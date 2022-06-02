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
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from jsonplaceholder_requests import get_userdata, get_posts
from models import Base, User, async_engine, Post, async_session


async def async_main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    
async def create_users(session: AsyncSession):
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        get_userdata(),
        get_posts(),
    )
    for list_data in users_data:
        session.add(User(name=list_data.get('name'),
                         username=list_data.get('username'),
                         email=list_data.get('email'),
                         )
                    )
        

        for post_dict_data in posts_data:
            session.add(Post(user_id=post_dict_data.get('userId'),
                             title=post_dict_data.get('title'),
                             body=post_dict_data.get('body')
                             )
                        )


    async def async_main():
        async with async_session() as session:
            await async_main()
            await create_users(session)



def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
