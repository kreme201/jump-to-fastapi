from pydantic import (
    BaseModel,
    field_validator,
    ValidationInfo,
    EmailStr,
    model_validator,
)


class UserResponse(BaseModel):
    username: str
    email: str

    class Config:
        from_attribute = True


class UserSave(BaseModel):
    username: str
    password: str
    password_chk: str
    email: EmailStr

    @field_validator("*")
    @classmethod
    def required(cls, v: str, info: ValidationInfo) -> str:
        if not v or not v.strip():
            raise ValueError(f"`{info.field_name} is required")
        return v.strip()

    @model_validator(mode="after")
    def password_equal(self) -> "UserSave":
        if self.password != self.password_chk:
            raise ValueError("password do not match")
        return self
