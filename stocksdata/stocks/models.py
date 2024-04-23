from datetime import date

from sqlalchemy import JSON, Column, String, Integer, Float, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Stocks(Base):
    __tablename__ = 'stocks'
    __table_args__ = {"schema": "stocksdata"}

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol = Column(String, nullable=False)
    amount = Column(Integer)
    status: Mapped[str]
    from_date = Mapped[Date]
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)
    afterHours = Mapped[float]
    preMarket = Mapped[float]
    performance = Mapped[JSON]

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}
