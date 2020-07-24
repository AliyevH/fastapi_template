from fastapi import APIRouter
from app.api.v1 import test_api

api_router = APIRouter()

api_router.include_router(test_api.router)