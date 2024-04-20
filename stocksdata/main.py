from http import HTTPStatus

from fastapi import FastAPI

from stocksdata.stocks.schemas.stock_post_request_schema import PostStockRequestSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World!'}


@app.post('/stock/{ticker}', status_code=HTTPStatus.CREATED)
def create_stocks_data(ticker: str, post_stock_schema: PostStockRequestSchema):
    return {
        'ticker': ticker,
        'amount': post_stock_schema.amount,
    }
