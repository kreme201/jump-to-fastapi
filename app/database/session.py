from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from app.database.context import get_db_session_context

SQLALCHEMY_DATABASE_URL = "sqlite:///../db.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
session_factory = sessionmaker(autoflush=False, autocommit=False, bind=engine)
session: Session | scoped_session = scoped_session(session_factory=session_factory, scopefunc=get_db_session_context)
