from datetime import datetime

from app.database import session, transactional
from app.schemas import Question


def get_question_list():
    return Question.query.all()


def get_question(question_id: int):
    return Question.query.get(question_id)


@transactional
def create_question(subject: str, content: str) -> Question:
    question = Question(subject=subject, content=content, created=datetime.now())
    session.add(question)
    return question


@transactional
def update_question(question_id: int, subject: str, content: str) -> Question:
    question = Question.query.get(question_id)
    question.subject = subject
    question.content = content
    question.updated = datetime.now()
    session.add(question)
    return question


@transactional
def delete_question(question_id: int) -> Question:
    question = Question.query.get(question_id)
    session.delete(question)
    return question
