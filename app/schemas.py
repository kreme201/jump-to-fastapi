from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Question(Base):
    __tablename__ = "pybo_question"

    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)


class Answer(Base):
    __tablename__ = "pybo_answer"

    content = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey("pybo_question.id"))
    question = relationship("Question", backref="answers")
