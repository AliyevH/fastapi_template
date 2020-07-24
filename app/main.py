from fastapi import FastAPI
from app.api.routers import api_router
from app.db.init_db import Base
import os

app = FastAPI()

app.include_router(api_router)


@app.on_event("startup",)
async def startup():
    print("app started")