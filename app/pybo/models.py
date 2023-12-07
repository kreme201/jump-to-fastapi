from datetime import datetime

from pydantic import BaseModel


class QuestionResponse(BaseModel):
    id: int
    subject: str
    content: str
    created: datetime
    updated: datetime | None


class QuestionSave(BaseModel):
    subject: str
    content: str
