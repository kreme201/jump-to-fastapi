from fastapi import APIRouter

router = APIRouter(prefix="/api/pybo")


@router.get("/")
def index():
    return {
        "message": "Hello Pybo",
    }
