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
import asyncio

from requests import Session
from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import USERS_DATA_URL, fetch_json, POSTS_DATA_URL
from models import Base, User, async_engine, Post



async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    users_data, posts_data = await asyncio.gather(fetch_json(USERS_DATA_URL), fetch_json(POSTS_DATA_URL))
    async with Session() as session:
        async with session.begin():
            for user in users_data:
                session.add(User(id=user['id'], name=user['name'], username=user['username'], email=user['email']))
            for post in posts_data:
                var = Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body'])
                session.add(var)


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    print("create user", user)
    session.add(user)
    await session.commit()
    return user

asyncio.run(async_main())

def main():
    pass


if __name__ == "__main__":
    main()
