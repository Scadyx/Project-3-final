import datetime

from sqlalchemy import text
from sqlalchemy.orm import Session


def get_order_status_stats_by_date(db: Session, dt: datetime.date):
    stmt = text("SELECT * FROM order_status_stats where dt = :dt")
    return db.execute(stmt, {'dt': dt})


def get_all_order_status_stats(db: Session):
    stmt = text("SELECT * FROM order_status_stats;")
    result = db.execute(stmt).all()
    return result
