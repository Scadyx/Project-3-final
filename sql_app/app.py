import datetime

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sql_app.database.database import SessionLocal, create_my_engine
from sql_app.cruds import sale_crud, order_status_crud, order_status_stats_crud
from sql_app.schemas.sale_class import Sale
from sql_app.schemas.order_status_class import OrderStatus

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    engine = create_my_engine()
    with open('data/create_tables.sql', 'r') as f:
        sql_create = f.read()
        engine.execute(sql_create)



@app.get("/")
async def root():
    return "Use /docs to open page with all endpoints"

# sale

@app.post("/sale", tags=["sales"])
async def create_sale(sale: Sale, db: Session = Depends(get_db)):
    return sale_crud.create_sale(db, sale)


@app.patch("/sale/{sale_id}", tags=["sales"])
async def update_sale(sale: Sale, sale_id: str, db: Session = Depends(get_db)):
    return sale_crud.update_sale_by_id(db, sale, sale_id)


@app.get("/sale", tags=["sales"])
def get_all_sales(db: Session = Depends(get_db)):
    return sale_crud.get_all_sales(db)


@app.get("/sale/{sale_id}", tags=["sales"])
def get_sale_by_id(sale_id: str, db: Session = Depends(get_db)):
    return sale_crud.get_sale_by_id(db, sale_id)


@app.delete("/sale/{sale_id}", tags=["sales"])
def delete_sale_by_id(sale_id: str, db: Session = Depends(get_db)):
    return sale_crud.delete_sale_by_id(db, sale_id)


@app.delete("/sale", tags=["sales"])
def delete_all_sales(db: Session = Depends(get_db)):
    return sale_crud.delete_all_sales(db)


# order_status_stats
@app.get("/order_status_stats", tags=["order_status_stats"])
def get_all_order_status_stats(db: Session = Depends(get_db)):
    return order_status_stats_crud.get_all_order_status_stats(db)


@app.get("/order_status_stats/{dt}", tags=["order_status_stats"])
def get_order_status_stats_by_dt(dt: datetime.date, db: Session = Depends(get_db)):
    return order_status_stats_crud.get_order_status_stats_by_date(db, dt)


# order_status
@app.get("/order_status", tags=["order_status"])
def get_all_order_statuses(db: Session = Depends(get_db)):
    return order_status_crud.get_all_order_statuses(db)


@app.get("/order_status/{order_status_id}", tags=["order_status"])
def get_order_status_by_id(order_status_id: str, db: Session = Depends(get_db)):
    return order_status_crud.get_order_status_by_id(db, order_status_id)


@app.delete("/order_status/{order_status_id}", tags=["order_status"])
def delete_order_status_by_id(order_status_id: str, db: Session = Depends(get_db)):
    return order_status_crud.delete_order_status_by_id(db, order_status_id)

@app.delete("/order_status", tags=["order_status"])
def delete_all_order_statuses(db: Session = Depends(get_db)):
    return order_status_crud.delete_all_order_statuses(db)


@app.patch("/order_status/{order_status_id}", tags=["order_status"])
def update_order_status(order_status_id: str, order_status: OrderStatus, db: Session = Depends(get_db)):
    return order_status_crud.update_order_status_by_id(db, order_status, order_status_id)


@app.post("/order_status", tags=["order_status"])
def create_order_status(order_status: OrderStatus, db: Session = Depends(get_db)):
    return order_status_crud.create_order_status(db, order_status)
