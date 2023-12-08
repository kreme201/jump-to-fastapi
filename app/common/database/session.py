from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from app.common.database.context import get_db_session_context
from app.config import DB_URL

engine = create_engine(DB_URL, connect_args={"check_same_thread": False}, echo=True)
session_factory = sessionmaker(autoflush=False, autocommit=False, bind=engine)
session: Session | scoped_session = scoped_session(
    session_factory=session_factory, scopefunc=get_db_session_context
)
