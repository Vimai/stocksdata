from datetime import date

from sqlalchemy import JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Stocks(Base):
    __tablename__ = 'stocks'
    __table_args__ = {"schema": "stocksdata"}

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str]
    from_date = Mapped[date]
    symbol = Mapped[str]
    open = Mapped[float]
    high = Mapped[float]
    low = Mapped[float]
    close = Mapped[float]
    volume = Mapped[int]
    amount = Mapped[int]
    afterHours = Mapped[float]
    preMarket = Mapped[float]
    performance = Mapped[JSON]
