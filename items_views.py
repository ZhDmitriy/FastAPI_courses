from typing import Annotated # позволяет комбинировать различные правила
from fastapi import APIRouter, Path


# tags=["Items"] - указываем для Свагера
router = APIRouter(prefix="/items", tags=["Items"])

# app существует только в основном файле, поэтому мы должны импортировать APIRouter()


@router.get("")
def list_items():
    return [
        "item1",
        "item2",
    ]


# возвращаем самый последний добавленный товар. Важен порядок, потому что мы добавляем latest в item_id и проверяем его на integer.
@router.get("/latest")
def get_latest_item():
    return {
        "item": {
            "id": "0",
            "name": "latest"
        }
    }


# параметры в пути
@router.get("/{item_id}")
# принимает число от 0 до 1_000_000
# 1_000_000 в Python не имеет значения
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]): # строгая валидация данных в FastAPI
    return {
        "item": {
            "id": item_id
        }
    }