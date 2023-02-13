from sqlalchemy import text
from sqlalchemy.orm import Session
from sql_app.schemas.order_status_class import OrderStatus


def create_order_status(db: Session, order_status: OrderStatus):
    query = text("insert into order_status (order_status_id, update_at, sale_id, status_name_id) "
                 "values (:order_status_id, :update_at, :sale_id, :status_name_id); ")
    db.execute(query, {'order_status_id': order_status.order_status_id,
                       'update_at': order_status.update_at,
                       'sale_id': order_status.sale_id,
                       'status_name_id': order_status.status_name_id})
    db.commit()
    return get_order_status_by_id(db, order_status.order_status_id)


def update_order_status_by_id(db: Session, order_status: OrderStatus, order_status_id: str):
    order_status_data = order_status.dict(exclude_unset=True)
    for key, value in order_status_data.items():
        stmt = text(f"UPDATE order_status SET {key} = '{value}' WHERE order_status_id = :order_status_id")
        db.execute(stmt, {'order_status_id': order_status_id})
        db.commit()
    return get_order_status_by_id(db, order_status_id)


def get_order_status_by_id(db: Session, order_status_id: str):
    stmt = text("SELECT * FROM order_status where order_status_id = :order_status_id;")
    return db.execute(stmt, {'order_status_id': order_status_id}).fetchall()


def get_all_order_statuses(db: Session):
    stmt = text("SELECT * FROM order_status;")
    result = db.execute(stmt).all()
    return result


def delete_all_order_statuses(db: Session):
    stmt = text("DELETE FROM order_status")
    db.execute(stmt)
    db.commit()
    return "all order_statuses deleted"


def delete_order_status_by_id(db: Session, order_status_id: str):
    order_status = get_order_status_by_id(db, order_status_id)
    stmt = text("DELETE FROM order_status where order_status_id = :order_status_id")
    db.execute(stmt, {'order_status_id': order_status_id})
    db.commit()
    return order_status
