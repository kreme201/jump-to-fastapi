import functools
import uuid
from contextvars import ContextVar, Token
from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from starlette.types import ASGIApp, Receive, Scope, Send

db_session_context: ContextVar[str] = ContextVar("db_session_context")


def get_db_session_context() -> str:
    return db_session_context.get()


def set_db_session_context(session_id: str) -> Token:
    return db_session_context.set(session_id)


def reset_db_session_context(context: Token) -> None:
    db_session_context.reset(context)


SQLALCHEMY_DATABASE_URL = "sqlite:///../db.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
session_factory = sessionmaker(autoflush=False, autocommit=False, bind=engine)
session: Union[Session, scoped_session] = scoped_session(session_factory=session_factory, scopefunc=get_db_session_context)
Base = declarative_base()
Base.query = session.query_property()


def transactional(func):
    @functools.wraps(func)
    def _transactional(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

        return result

    return _transactional


class SqlAlchemySessionMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        session_id = str(uuid.uuid4())
        context = set_db_session_context(session_id)

        try:
            await self.app(scope, receive, send)
        except Exception as e:
            raise e
        finally:
            session.remove()
            reset_db_session_context(context)
