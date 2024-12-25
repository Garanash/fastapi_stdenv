from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr
from .base import Base


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[str]
