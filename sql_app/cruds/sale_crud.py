from sqlalchemy import text
from sqlalchemy.orm import Session
from sql_app.schemas.sale_class import Sale


def create_sale(db: Session, sale: Sale):
    query = "insert into sale (sale_id, date_sale, amount, product_id, user_id, store_id) values (:sale_id, :date_sale, :amount, :product_id, :user_id, :store_id);"
    db.execute(text(query), {
        "sale_id": sale.sale_id,
        "date_sale": sale.date_sale,
        "amount": sale.amount,
        "product_id": sale.product_id,
        "user_id": sale.user_id,
        "store_id": sale.store_id
    })
    db.commit()
    return get_sale_by_id(db, sale.sale_id)


def update_sale_by_id(db: Session, sale: Sale, sale_id: str):
    sale_data = sale.dict(exclude_unset=True)
    for key, value in sale_data.items():
        stmt = text(f"UPDATE sale SET {key} = '{value}' WHERE sale_id = :sale_id")
        db.execute(stmt, {'sale_id': sale_id})
        db.commit()
    return get_sale_by_id(db, sale.sale_id)

def get_sale_by_id(db: Session, sale_id: str):
    stmt = text("SELECT * FROM sale where sale_id = :sale_id")
    return db.execute(stmt, {'sale_id': sale_id}).fetchall()


def delete_sale_by_id(db: Session, sale_id: str):
    sale = get_sale_by_id(db, sale_id)
    stmt = text("DELETE FROM sale where sale_id = :sale_id")
    db.execute(stmt, {'sale_id': sale_id})
    db.commit()
    return sale


def get_all_sales(db: Session):
    stmt = text("SELECT * FROM sale;")
    result = db.execute(stmt).all()
    return result


def delete_all_sales(db: Session):
    stmt = text("DELETE FROM order_status")
    db.execute(stmt)
    stmt = text("DELETE FROM sale;")
    db.execute(stmt)
    db.commit()
    return "all sales deleted"
