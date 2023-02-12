from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import OrderStatusCreate


def create_order_status(order_status: OrderStatusCreate):
    query = f"insert into order_status (update_at, sale_id) values ('{order_status.update_at}', '{order_status.sale_id}'," \
            f" '{order_status.status_name_id}') RETURNING order_status_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("order_status", order_status_id=row['order_status_id'])


def upupdate_at_by_id(order_status: schemas.OrderStatus):
    query = f"update order_status set update_at = '{order_status.update_at}', status_name_id = '{order_status.status_name_id}', sale_id = '{order_status.sale_id}'" \
            f" where order_status_id = {order_status.order_status_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("users", order_status_id=order_status.order_status_id)
