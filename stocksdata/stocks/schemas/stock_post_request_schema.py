from pydantic import BaseModel


class PostStockRequestSchema(BaseModel):
    amount: int
