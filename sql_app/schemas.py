
from typing import Union
from pydantic import BaseModel
from pydantic.schema import datetime


class ProductCreate(BaseModel):
    name: str


class Product(ProductCreate):
    product_id: int


class CountryCreate(BaseModel):
    country_name: int


class Country(CountryCreate):
    country_id: int


class CityCreate(BaseModel):
    city_name: str
    country_id: int


class City(CityCreate):
    city_id: int


class StoreCreate(BaseModel):
    name: str
    city_id: int


class Store(StoreCreate):
    store_id: int


class UserCreate(BaseModel):
    name: str


class User(UserCreate):
    user_id: int
    

class StatusNameCreate(BaseModel):
    status_name: str


class StatusName(StatusNameCreate):
    status_name_id: int


class SaleCreate(BaseModel):
    amount: float
    date_sale: Union[datetime, None] = None
    product_id: int
    user_id: int
    store_id: int


class Sale(SaleCreate):
    sale_id: str


class OrderStatusCreate(BaseModel):
    update_at: Union[datetime, None] = None
    sale_id: str
    status_name_id: int


class OrderStatus(OrderStatusCreate):
    order_status_id: str


class OrderStatusStatsCreate(BaseModel):
    dt: datetime.date
    order_status_name: str
    orders_count: int





