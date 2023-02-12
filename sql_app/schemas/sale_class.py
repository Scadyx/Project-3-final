from datetime import date
from typing import Union

from pydantic import BaseModel


class Sale(BaseModel):
    amount: float
    date_sale: Union[date, None] = None
    product_id: int
    user_id: int
    store_id: int

