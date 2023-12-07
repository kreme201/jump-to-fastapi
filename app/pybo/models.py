from datetime import datetime

from pydantic import BaseModel


class AnswerResponse(BaseModel):
    id: int
    content: str
    created: datetime
    updated: datetime | None

    class Config:
        from_attribute = True


class QuestionResponse(BaseModel):
    id: int
    subject: str
    content: str
    created: datetime
    updated: datetime | None
    answers: list[AnswerResponse] = []

    class Config:
        from_attribute = True


class QuestionSave(BaseModel):
    subject: str
    content: str


class AnswerSave(BaseModel):
    content: str
