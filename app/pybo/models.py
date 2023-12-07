from datetime import datetime

from pydantic import BaseModel, field_validator, ValidationInfo


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

    @field_validator("subject", "content")
    @classmethod
    def required(cls, v: str, info: ValidationInfo) -> str:
        if not v or not v.strip():
            raise ValueError(f"'{info.field_name}' field is required")
        return v.strip()


class AnswerSave(BaseModel):
    content: str

    @field_validator("content")
    @classmethod
    def required(cls, v: str, info: ValidationInfo) -> str:
        if not v or not v.strip():
            raise ValueError(f"'{info.field_name}' field is required")
        return v.strip()
