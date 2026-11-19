from pydantic import BaseModel, Field, ConfigDict, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    role: str
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    role: str = Field(default='master', pattern='^(master|admin)$')
    