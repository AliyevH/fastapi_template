from fastapi import APIRouter, Body
from starlette.responses import JSONResponse
from app.core.settings import settings
from app.models import user_model

router = APIRouter()


@router.get("/",
            tags=["Test"],
            response_description="test",
            include_in_schema=settings.INCLUDE_SCHEMA,
)
async def test() -> JSONResponse:
    return JSONResponse({"result": "True"})

