from fastapi import FastAPI
from .routes import router as copilot_router
from .db import init_db


def create_app():
    app = FastAPI(title="Copilot Service (Invoice AI)")
    init_db()
    app.include_router(copilot_router, prefix="/copilot")
    return app


app = create_app()
