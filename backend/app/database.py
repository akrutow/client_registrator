from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os


load_dotenv()
secret = os.getenv('SECRET')
host = os.getenv('API_HOST', '127.0.0.1')

DATABASE_URL = f'postgresql+asyncpg://registrator_user:{secret}@{host}:5432/registrator_db'

async_engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass
