from fastapi import FastAPI

from app.pybo import pybo_routes

app = FastAPI()

app.include_router(pybo_routes.router)


@app.get("/")
def index():
    return {
        "message": "Hello World",
    }
