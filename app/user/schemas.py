from sqlalchemy import Column, String

from app.common.database.base import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
