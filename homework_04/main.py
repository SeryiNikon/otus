"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from models import Base, User


async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:password@localhost/postgres",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async def create_user(session: AsyncSession, username: str) -> User:
        user = User(username=username)
        print("create user", user)
        session.add(user)

        await session.commit()
        return user


    pass


def main():
    pass


if __name__ == "__main__":
    main()
