from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from items_views import router as items_router
from users.views import router as users_router
import uvicorn

# Основное приложение

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


class CreateUser(BaseModel):
    email: EmailStr


# создаем представление с методом get
@app.get("/") # endpoint
def hello_index():
    return {
        "message": "hello index!"
    }


# redirect - обновление запроса с нужными параметрами


# передача параметров в строке параметров
@app.get("/hello/")
def hello(name: str = "World!"):
    name = name.strip().title()
    return {
        "message": f"Hello {name}"
    }


@app.post("/users")
def create_user(user: CreateUser): # валидация email из встроенной библиотеки в FastAPI
    return {
        "message": "success",
        "email": user.email
    }


@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "a + b = ": a + b
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=5000) # можем указать порт вручную
    # netstat -a - посмотреть все порты которые сейчас что-то обрабатывают в cmd

