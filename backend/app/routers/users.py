from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.app.models.users import User as UserModel
from backend.app.schemas.users import UserCreate, User as UserSchema
from backend.app.db_depends import get_async_db
from backend.app.auth import hash_password


router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_async_db)):
    '''Регистрирует нового пользователя.'''
    result = await db.scalars(select(UserModel).where(UserModel.email == user.email))
    if result.first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Email already registered')
    db_user = UserModel(
        email=user.email,
        hashed_password=hash_password(user.password),
    )
    db.add(db_user)
    await db.commit()
    return db_user