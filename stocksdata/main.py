from http import HTTPStatus

import redis
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from stocksdata.PolygonApiClient import PolygonApiClient
from stocksdata.database import get_session
from stocksdata.settings import Settings
from stocksdata.stocks.schemas.stock_post_request_schema import PostStockRequestSchema
from stocksdata.stocks.service import StocksService

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World!'}


@app.post('/stock/{ticker}', status_code=HTTPStatus.CREATED)
def create_stocks_data(ticker: str, post_stock_schema: PostStockRequestSchema, session: Session = Depends(get_session)):
    service = StocksService(
        session=session,
        api_client=PolygonApiClient(
            host=Settings().POLYGON_HOST,
            api_key=Settings().POLYGON_API_KEY,
        ),
        redis_client=redis.Redis(host=Settings().REDIS_HOST, port=6379, db=0)
    )
    return service.save_amount(ticker, post_stock_schema.amount)


@app.get('/stock/{ticker}', status_code=HTTPStatus.OK)
def create_stocks_data(ticker: str, session: Session = Depends(get_session)):
    service = StocksService(
        session=session,
        api_client=PolygonApiClient(
            host=Settings().POLYGON_HOST,
            api_key=Settings().POLYGON_API_KEY,
        ),
        redis_client=redis.Redis(host=Settings().REDIS_HOST, port=6379, db=0)
    )
    return service.search(ticker)
