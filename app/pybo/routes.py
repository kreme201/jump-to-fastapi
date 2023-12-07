from fastapi import APIRouter

from app.pybo import service as pybo_service
from app.pybo.models import QuestionResponse

router = APIRouter(prefix="/api/pybo", tags=["Pybo"])


@router.get("/", response_model=list[QuestionResponse])
def question_list():
    return pybo_service.get_question_list()


@router.get("/{question_id}", response_model=QuestionResponse)
def question_get(question_id: int):
    return pybo_service.get_question(question_id)


@router.post("/", response_model=QuestionResponse)
def question_register(subject: str, content: str):
    return pybo_service.create_question(subject, content)


@router.put("/{question_id}", response_model=QuestionResponse)
def question_update(question_id: int, subject: str, content: str):
    return pybo_service.update_question(question_id, subject, content)


@router.delete("/{question_id}", response_model=QuestionResponse)
def question_delete(question_id: int):
    return pybo_service.delete_question(question_id)
