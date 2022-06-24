from fastapi import APIRouter

import settings


router = APIRouter()


@router.get("/", tags=["home"], description="home endpoint")
def home():
    return {"environment": settings.ENV}
