from app.common.database.decorators import transactional
from app.pybo.schemas import Question, Answer


def get_question_list():
    return Question.query.all()


def get_question(question_id: int):
    question = Question.query.get(question_id)
    if question is None:
        raise ValueError("Not Found")
    return question


@transactional
def create_question(subject: str, content: str) -> Question:
    return Question(subject=subject, content=content).save()


@transactional
def update_question(question_id: int, subject: str, content: str) -> Question:
    question = get_question(question_id)
    question.subject = subject
    question.content = content
    return question.save()


@transactional
def delete_question(question_id: int) -> Question:
    return get_question(question_id).delete()


@transactional
def create_answer(question_id: int, content: str) -> Answer:
    return Answer(question_id=question_id, content=content).save()


def get_answer(answer_id: int) -> Answer | None:
    answer = Answer.query.get(answer_id)

    if answer is None:
        raise ValueError("Not Found")

    return answer


@transactional
def update_answer(answer_id: int, content: str) -> Answer:
    answer = get_answer(answer_id)
    answer.content = content
    return answer.save()


@transactional
def delete_answer(answer_id: int) -> Answer:
    return get_answer(answer_id).delete()
