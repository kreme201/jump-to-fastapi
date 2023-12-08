from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.database.middlewares import SqlAlchemySessionMiddleware
from app.pybo.routes import router as pybo_router
from app.user.routes import router as user_router

app = FastAPI()

# Middlewares
app.add_middleware(SqlAlchemySessionMiddleware)


@app.exception_handler(Exception)
def exception_handler(request: Request, e: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(
            {
                "detail": str(e),
            }
        ),
    )


# Routes
app.include_router(pybo_router, prefix="/api/pybo", tags=["Pybo"])
app.include_router(user_router, prefix="/api/user", tags=["User"])
