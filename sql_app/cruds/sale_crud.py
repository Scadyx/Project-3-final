from sqlalchemy import text
from sqlalchemy.orm import Session
from sql_app.schemas.sale_class import Sale


def create_sale(db: Session, sale: Sale):
    query = "insert into sale (date_sale, amount, product_id, user_id, store_id) values (:date_sale, :amount, :product_id, :user_id, :store_id) RETURNING sale_id"
    db.session.execute(text(query), {
        "date_sale": sale.date_sale,
        "amount": sale.amount,
        "product_id": sale.product_id,
        "user_id": sale.user_id,
        "store_id": sale.store_id
    })
    db.commit()
    return sale
    # return get_sale_by_id(db, result)


def update_sale_by_id(db: Session, sale: Sale, sale_id: str):
    bet_data = sale.dict(exclude_unset=True)
    for key, value in bet_data.items():
        stmt = text(f"UPDATE sale SET {key} = '{value}' WHERE sale_id = :sale_id")
        db.execute(stmt, {'sale_id': sale_id})
        db.commit()


def get_sale_by_id(db: Session, sale_id: str):
    stmt = text("SELECT * FROM sale where sale_id = :sale_id")
    return db.execute(stmt, {'sale_id': sale_id})


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
    # First set all references in order_status table to 'null'
    stmt = text("DELETE FROM order_status")
    db.execute(stmt)
    # Then delete all rows from the sale table
    stmt = text("DELETE FROM sale;")
    db.execute(stmt)
    db.commit()
    return "all sales deleted"
