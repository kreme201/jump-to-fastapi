from fastapi import FastAPI

from app.database import SqlAlchemySessionMiddleware
from app.pybo import pybo_routes

app = FastAPI()

# Middlewares
app.add_middleware(SqlAlchemySessionMiddleware)

# Routes
app.include_router(pybo_routes.router)
