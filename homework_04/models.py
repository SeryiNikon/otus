"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
async_engine = create_async_engine(
    PG_CONN_URI,
    echo=True,
)

#Base = None
Base = declarative_base(async_engine)

#Session = None
async_session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

class User(Base):
    __tablename__ = 'Users'
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = 'Posts'
    user_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    body = Column(String(100), nullable=False)
    user = relationship("User", back_populates="posts")
