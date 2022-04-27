from fastapi import APIRouter


router = APIRouter()


@router.get('/', tags=['home'], description='home endpoint')
def home():
    return {'environment': 'development'}