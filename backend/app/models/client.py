from sqlalchemy import ForeignKey, Integer, String, Boolean, Numeric
from sqlalchemy.orm import mapped_column, Mapped, relationship
from decimal import Decimal

from backend.app.database import Base


class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    phone_number: Mapped[str | None] = mapped_column(String, nullable=True)
    link: Mapped[str | None] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)

    user: Mapped['User'] = relationship('User', back_populates='clients')