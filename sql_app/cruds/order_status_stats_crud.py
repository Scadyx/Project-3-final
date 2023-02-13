import datetime

from sqlalchemy import text
from sqlalchemy.orm import Session


def get_order_status_stats_by_date(db: Session, dt: datetime.date):
    dt_str = dt.strftime("%Y-%m-%d")
    stmt = text("SELECT * FROM order_status_stats where dt = :dt")
    return db.execute(stmt, {'dt': dt_str}).fetchall()


def get_all_order_status_stats(db: Session):
    stmt = text("SELECT * FROM order_status_stats;")
    result = db.execute(stmt).all()
    return result
