"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from typing import Dict

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_userdata() -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            userdata: dict = await resp.json()
            return userdata


async def get_posts() -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as resp:
            postdata: dict = await resp.json()
            return postdata

#async def fetch_json(url):
#    async with aiohttp.ClientSession() as session:
#        async with session.get(url) as response:
#            return await response.json()


#if __name__ == '__main__':
#    asyncio.run(fetch_json(USERS_DATA_URL))
#    asyncio.run(fetch_json(POSTS_DATA_URL))
