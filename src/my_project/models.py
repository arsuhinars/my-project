from enum import StrEnum

from sqlalchemy.orm import Mapped, mapped_column

from my_project.db import Base


class UserRole(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    name: Mapped[str]
    role: Mapped[UserRole]
    email: Mapped[str]
    password: Mapped[str]
