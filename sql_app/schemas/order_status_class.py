import datetime
from typing import Union

from pydantic import BaseModel


class OrderStatus(BaseModel):
    order_status_id: str
    update_at: Union[datetime.datetime, None] = None
    sale_id: str
    status_name_id: int