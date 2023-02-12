import datetime
from typing import Union

from pydantic import BaseModel


class Sale(BaseModel):
    sale_id: str
    amount: float
    date_sale: Union[datetime.datetime, None] = None
    product_id: int
    user_id: int
    store_id: int

