from fastapi import APIRouter

from app.user import services as user_service
from app.user.models import UserSave, UserResponse

router = APIRouter()


@router.post("/", response_model=UserResponse)
def user_create(dto: UserSave):
    return user_service.create_user(
        username=dto.username,
        email=dto.email,
        password=dto.password,
    )
