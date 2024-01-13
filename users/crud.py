"""

    Модуль, где происходят все действия не только с базой данных, но и с объектами приложения:
    - Создание
    - Чтение
    - Удаление
    - Обновление

"""
from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump() # делаем словарь из данных
    return {
        "success": True,
        "user": user
    }

