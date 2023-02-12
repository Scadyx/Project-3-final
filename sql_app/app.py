from datetime import datetime

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sql_app.database.database import SessionLocal
from sql_app.cruds import sale_crud
from sql_app.schemas.sale_class import Sale

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
def get_all_order_status_stats():
    return common.get("order_status_stats")


@app.get("/order_status_stats/{dt}", tags=["order_status_stats"])
def get_order_status_stats_by_dt(dt: datetime):
    return common.get("order_status_stats", dt=f"'{dt}'")


# order_status
@app.get("/order_status", tags=["order_status"])
def get_all_order_statuses():
    return common.get("order_status")


@app.get("/order_status/{order_status_id}", tags=["order_status"])
def get_order_status_by_id(order_status_id: str):
    return common.get("order_status", order_status_id=order_status_id)


@app.delete("/order_status/{store_id}", tags=["order_status"])
def delete_order_status_by_id(order_status_id: str):
    return common.delete("order_status", order_status_id=order_status_id)


@app.delete("/order_status", tags=["order_status"])
def delete_all_order_statuses():
    return common.delete("order_status")


@app.patch("/order_status", tags=["order_status"])
def update_order_status():
    return common.delete("order_status")


@app.post("/order_status", tags=["order_status"])
def create_order_status():
    return common.delete("order_status")
