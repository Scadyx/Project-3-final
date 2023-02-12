import datetime
from typing import Union

from pydantic import BaseModel


class OrderStatus(BaseModel):
    update_at: Union[datetime, None] = None
    sale_id: str
    status_name_id: int