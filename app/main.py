from fastapi import FastAPI

from app.database.middlewares import SqlAlchemySessionMiddleware
from app.pybo.routes import router as pybo_router

app = FastAPI()

# Middlewares
app.add_middleware(SqlAlchemySessionMiddleware)

# Routes
app.include_router(pybo_router, prefix="/api/pybo")
