from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Product(Declarative_base):
    __abstract__ = True
    id: Mapped[int]
