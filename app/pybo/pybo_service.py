from datetime import datetime

from app.database import transactional
from app.schemas import Question


def get_question_list():
    return Question.query.all()


def get_question(question_id: int):
    return Question.query.get(question_id)


@transactional
def create_question(subject: str, content: str) -> Question:
    question = Question(subject=subject, content=content, created=datetime.now())
    return question.save()


@transactional
def update_question(question_id: int, subject: str, content: str) -> Question:
    question = Question.query.get(question_id)
    question.subject = subject
    question.content = content
    question.updated = datetime.now()
    return question.save()


@transactional
def delete_question(question_id: int) -> Question:
    question = Question.query.get(question_id)
    return question.delete()
