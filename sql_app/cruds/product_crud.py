from fastapi_sqlalchemy import db
from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import ProductCreate


def create_product(product: ProductCreate):
    query = f"insert into products (name) values ('{product.name}') RETURNING product_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("products", product_id=row['product_id'])


def update_product_by_id(product: schemas.Product):
    query = f"update products set name = '{product.name}' where product_id = {product.product_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("products", product_id=product.product_id)





