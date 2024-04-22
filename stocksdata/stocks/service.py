from datetime import date

from stocksdata.stocks.models import Stocks


class StocksService:
    def __init__(self, session, api_client):
        self.session = session
        self.__api_client = api_client
        return

    def search(self, ticker: str):
        results = self.session.query(Stocks).filter(Stocks.symbol == ticker).all()
        return results

    def save_amount(self, ticker: str, amount: int):
        open_close_data = self.__api_client.get_open_close_data(
            ticker=ticker,
            data=date.today()
        )

        stocks = Stocks(
            symbol=ticker,
            amount=amount,
        )

        if open_close_data:
            stocks.status = open_close_data.get('status')
            stocks.from_date = open_close_data.get('from_date')
            stocks.open = open_close_data.get('open')
            stocks.close = open_close_data.get('close')
            stocks.high = open_close_data.get('high')
            stocks.low = open_close_data.get('low')
            stocks.volume = open_close_data.get('volume')
            stocks.afterHours = open_close_data.get('afterHours')
            stocks.preMarket = open_close_data.get('preMarket')

        stocks.performance = {}

        self.session.add(stocks)
        self.session.commit()
        self.session.refresh(stocks)
        return stocks
