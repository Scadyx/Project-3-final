from datetime import datetime

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from sql_app import schemas
from sql_app.database import SQLALCHEMY_DATABASE_URL
from sql_app.cruds import users_crud, common
from sql_app.schemas import UserCreate

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABASE_URL)


@app.get("/")
async def root():
    return "Use /docs to open page with all endpoints"


# product
@app.get("/product")
def get_all_products():
    return common.get("product")


@app.get("/product/{product_id}")
def get_product_by_id(product_id: int):
    return common.get("product", product_id=product_id)


@app.delete("/product/{product_id}")
def delete_product_by_id(product_id: int):
    return common.delete("product", product_id=product_id)


@app.delete("/product")
def delete_all_product():
    return common.delete("product")


# country
@app.get("/country")
def get_all_countries():
    return common.get("country")


@app.get("/country/{country_id}")
def get_country_by_id(country_id: int):
    return common.get("country", country_id=country_id)


@app.delete("/country/{country_id}")
def delete_country_by_id(country_id: int):
    return common.delete("country", country_id=country_id)


@app.delete("/country")
def delete_all_countries():
    return common.delete("country")


# city
@app.get("/city")
def get_all_cities():
    return common.get("city")


@app.get("/city/{city_id}")
def get_city_by_id(city_id: int):
    return common.get("city", city_id=city_id)


@app.delete("/city/{city_id}")
def delete_city_by_id(city_id: int):
    return common.delete("city", city_id=city_id)


@app.delete("/city")
def delete_all_cities():
    return common.delete("city")


# store
@app.get("/store")
def get_all_stores():
    return common.get("store")


@app.get("/store/{store_id}")
def get_store_by_id(store_id: int):
    return common.get("store", store_id=store_id)


@app.delete("/store/{store_id}")
def delete_store_by_id(store_id: int):
    return common.delete("store", store_id=store_id)


@app.delete("/store")
def delete_all_stores():
    return common.delete("store")


# users
@app.get("/users")
def get_all_users():
    return common.get("users")


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return common.get("users", user_id=user_id)


@app.post("/users")
def create_user(user: UserCreate):
    return users_crud.create_user(user)


@app.put("/users")
def update_user_by_id(user: schemas.User):
    return users_crud.update_user_by_id(user)


@app.delete("/users/{user_id}")
def delete_user_by_id(user_id: int):
    return common.delete("users", user_id=user_id)


@app.delete("/users")
def delete_all_users():
    return common.delete("users")


# status_name
@app.get("/status_name")
def get_all_status_names():
    return common.get("status_name")


@app.get("/status_name/{status_name_id}")
def get_status_name_by_id(status_name_id: int):
    return common.get("status_name", status_name_id=status_name_id)


@app.delete("/status_name/{status_name_id}")
def delete_status_name_by_id(status_name_id: int):
    return common.delete("status_name", status_name_id=status_name_id)


@app.delete("/status_name")
def delete_all_status_names():
    return common.delete("status_name")


# sale
@app.get("/sale")
def get_all_sales():
    return common.get("sale")


@app.get("/sale/{store_id}")
def get_sale_by_id(sale_id: str):
    return common.get("sale", sale_id=sale_id)


@app.delete("/sale/{store_id}")
def delete_sale_by_id(sale_id: str):
    return common.delete("sale", sale_id=sale_id)


@app.delete("/sale")
def delete_all_sales():
    return common.delete("sale")


# order_status
@app.get("/order_status")
def get_all_order_statuses():
    return common.get("order_status")


@app.get("/order_status/{order_status_id}")
def get_order_status_by_id(order_status_id: str):
    return common.get("order_status", order_status_id=order_status_id)


@app.delete("/order_status/{store_id}")
def delete_order_status_by_id(order_status_id: str):
    return common.delete("order_status", order_status_id=order_status_id)


@app.delete("/order_status")
def delete_all_order_statuses():
    return common.delete("order_status")


# order_status_stats
@app.get("/order_status_stats")
def get_all_order_status_stats():
    return common.get("order_status_stats")


@app.get("/order_status_stats/{dt}")
def get_order_status_stats_by_dt(dt: datetime):
    return common.get("order_status_stats", dt=f"'{dt}'")