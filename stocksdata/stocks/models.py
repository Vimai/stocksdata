from datetime import date

from sqlalchemy import JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Stocks(Base):
    __tablename__ = 'stocks'
    __table_args__ = {"schema": "stocksdata"}

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol = Mapped[str]
    amount = Mapped[int]
    status: Mapped[str]
    from_date = Mapped[date]
    open = Mapped[float]
    close = Mapped[float]
    high = Mapped[float]
    low = Mapped[float]
    volume = Mapped[int]
    afterHours = Mapped[float]
    preMarket = Mapped[float]
    performance = Mapped[JSON]
