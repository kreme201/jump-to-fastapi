from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

from app.auth.models import Token
from app.common.contexts import pwd_context
from app.user import services as user_service

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "TEST"
ALGORITHM = "HS256"
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


@router.post("/login", response_model=Token)
def get_access_token(dto: OAuth2PasswordRequestForm = Depends()):
    user = user_service.get_user_by_username(dto.username)

    if not user or not pwd_context.verify(dto.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={
                "WWW-Authenticate": "Bearer",
            },
        )

    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return Token(
        access_token=access_token,
        token_type="bearer",
        username=user.username,
    )


def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer",
        },
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception
    else:
        user = user_service.get_user_by_username(username)

        if user is None:
            raise credentials_exception
        return user
