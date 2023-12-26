from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
import datetime
from db.database import Base


class Users(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(String(30))
    start: Mapped[bool] = mapped_column(default=True)


class Apartment(Base):
    __tablename__ = "apartment"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_apartment: Mapped[int]
    name: Mapped[str] = mapped_column(String(30))
    created_at = Mapped[datetime.datetime]
