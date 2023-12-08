from app.common.contexts import pwd_context
from app.common.database.decorators import transactional
from app.user.exceptions import UserNotFoundException, UserAlreadyExistsException
from app.user.schemas import User


def get_user(user_id: int) -> User:
    user = User.query.get(user_id)

    if user is None:
        raise UserNotFoundException

    return user


def get_user_by_username(username: str) -> User:
    user = User.query.filter(User.username == username).first()

    if user is None:
        raise UserNotFoundException

    return user


@transactional
def create_user(username: str, email: str, password: str) -> User:
    if (
        User.query.filter(User.username == username or User.email == email).first()
        is not None
    ):
        raise UserAlreadyExistsException

    return User(
        username=username,
        email=email,
        password=pwd_context.hash(password),
    ).save()


@transactional
def update_user(user_id: int, email: str = "", password: str = "") -> User:
    user = get_user(user_id)

    if email.strip():
        user.email = email.strip()
    if password.strip():
        user.password = pwd_context.hash(password.strip())

    return user.save()


@transactional
def delete_user(user_id: int) -> User:
    return get_user(user_id).delete()
