
from typing import Union
from pydantic import BaseModel
from pydantic.schema import datetime


class Sale(BaseModel):
    sale_id: str
    amount: float
    date_sale: Union[int, None] = None
    product_id: int
    user_id: int
    store_id: int


class OrderStatusStats(BaseModel):
    dt: datetime.date
    order_status_name: str
    orders_count: int


class UserBase(BaseModel):

    age: Union[int, None] = None
    balance: Union[float, None] = None
    birth_day: Union[str, None] = None
    city: Union[str, None] = None
    gender: Union[str, None] = None
    ip: Union[str, None] = None
    last_name: Union[str, None] = None
    name: Union[str, None] = None
    premium: Union[bool, None] = None
    time_created: Union[int, None] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int


class BetBase(BaseModel):
    date_created: Union[datetime.date, None] = None
    user_id: int
    event_id: int


class BetCreate(BetBase):
    pass


class Bet(BetBase):
    id: int


class EventBase(BaseModel):
    type: Union[str, None] = None
    name: Union[str, None] = None
    event_date: Union[datetime.date, None] = None


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
