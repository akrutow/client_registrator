from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.app.models.users import User as UserModel
from backend.app.schemas.users import UserCreate, User as UserSchema
from backend.app.db_depends import get_async_db
from backend.app.auth import hash_password


router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user():
    pass