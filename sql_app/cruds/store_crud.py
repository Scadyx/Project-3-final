from fastapi_sqlalchemy import db
from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import StoreCreate


def create_store(store: StoreCreate):
    query = f"insert into stores (name, city_id) values ('{store.name}', '{store.city_id}') RETURNING store_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("stores", store_store_id=row['store_store_id'])


def update_store_by_store_id(store: schemas.Store):
    query = f"update stores set name = '{store.name}', city_id = '{store.city_id}' where store_id = {store.store_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("stores", store_store_id=store.store_id)





