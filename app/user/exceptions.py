from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = None):
        if detail is None or detail == "":
            detail = "User not found"

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class UserAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = None):
        if detail is None or detail == "":
            detail = "User already exists"

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
        )
