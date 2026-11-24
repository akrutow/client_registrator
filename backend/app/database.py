from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import settings

engine = create_async_engine(settings.database_url, echo=True)  # echo=True — лог SQL в консоль, для обучения полезно
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Базовый класс для всех моделей."""


async def get_session() -> AsyncIterator[AsyncSession]:
    """Dependency для FastAPI: одна сессия на запрос."""
    async with async_session() as session:
        yield session