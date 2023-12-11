from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import text, String
import enum
import datetime
from typing import Optional


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
    name: Mapped[str] = mapped_column(String(30))
    start: Mapped[bool]


class Apartment(Base):
    __tablename__ = "apartment"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_apartment: Mapped[int]
    name: Mapped[str] = mapped_column(String(30))
    created_at = Mapped[datetime.datetime]

    user: Mapped["User"] = relationship(back_populates="addresses")
