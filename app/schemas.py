from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Question(Base):
    __tablename__ = "pybo_question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=True)


class Answer(Base):
    __tablename__ = "pybo_answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=True)
    question_id = Column(Integer, ForeignKey("pybo_question.id"))
    question = relationship("Question", backref="answers")
