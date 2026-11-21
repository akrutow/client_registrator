from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal


class Client(BaseModel):
    pass


class ClientCreate(BaseModel):
    name: str
    date: str
    price: Decimal
    link: str | None = Field(default=None)