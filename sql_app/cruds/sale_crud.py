from fastapi_sqlalchemy import db
from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import SaleCreate


def create_sale(sale: SaleCreate):
    query = f"insert into sales (date_sale, amount, product_id, user_id, store_id) " \
            f"values ('{sale.date_sale}', '{sale.amount}', '{sale.product_id}', '{sale.user_id}', '{sale.store_id}') RETURNING sale_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("sale", sale_id=row['sale_id'])


def update_sale_by_id(sale: schemas.Sale):
    query = f"update sales set date_sale = '{sale.date_sale}', product_id = '{sale.product_id}', amount = '{sale.amount}'" \
            f", user_id = '{sale.user_id}', store_id = '{sale.store_id}'" \
            f" where sale_id = {sale.sale_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("users", sale_id=sale.sale_id)
