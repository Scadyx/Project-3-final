import datetime

from pydantic import BaseModel


class OrderStatusStats(BaseModel):
    dt: datetime.datetime
    order_status_name: str
    orders_count: int