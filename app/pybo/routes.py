from fastapi import APIRouter

from app.pybo import services as pybo_service
from app.pybo.models import QuestionResponse, QuestionSave, AnswerResponse, AnswerSave

router = APIRouter()


@router.get("/question", response_model=list[QuestionResponse])
def question_list():
    return pybo_service.get_question_list()


@router.get("/question/{question_id}", response_model=QuestionResponse)
def question_get(question_id: int):
    return pybo_service.get_question(question_id)


@router.post("/question", response_model=QuestionResponse)
def question_register(dto: QuestionSave):
    return pybo_service.create_question(dto.subject, dto.content)


@router.put("/question/{question_id}", response_model=QuestionResponse)
def question_update(question_id: int, dto: QuestionSave):
    return pybo_service.update_question(question_id, dto.subject, dto.content)


@router.delete("/question/{question_id}", response_model=QuestionResponse)
def question_delete(question_id: int):
    return pybo_service.delete_question(question_id)


@router.post("/answer/{question_id}", response_model=AnswerResponse)
def answer_create(question_id: int, dto: AnswerSave):
    return pybo_service.create_answer(question_id, dto.content)


@router.put("/answer/{answer_id}", response_model=AnswerResponse)
def answer_update(answer_id: int, dto: AnswerSave):
    return pybo_service.update_answer(answer_id, dto.content)


@router.delete("/answer/{answer_id}", response_model=AnswerResponse)
def answer_delete(question_id: int, answer_id: int):
    return pybo_service.delete_answer(question_id, answer_id)
