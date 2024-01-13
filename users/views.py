from fastapi import APIRouter
from users.schemas import CreateUser
from users import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: CreateUser): # валидация email из встроенной библиотеки в FastAPI
    return crud.create_user(user_in=user)