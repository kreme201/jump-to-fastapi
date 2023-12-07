import functools
from contextvars import ContextVar, Token
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session

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
session: Session | scoped_session = scoped_session(session_factory=session_factory, scopefunc=get_db_session_context)


class CustomBase:
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=True)

    def save(self):
        if self.id is None:
            self.created = datetime.now()
        else:
            self.updated = datetime.now()

        session.add(self)
        return self

    def delete(self):
        session.delete(self)
        return self


Base = declarative_base(cls=CustomBase)
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
