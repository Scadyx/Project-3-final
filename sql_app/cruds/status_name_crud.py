from fastapi_sqlalchemy import db
from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import StatusNameCreate


def create_status_name(status_name: StatusNameCreate):
    query = f"insert into status_names (name) " \
            f"values ('{status_name.status_name}') RETURNING status_name_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("status_names", status_name_id=row['status_name_id'])


def update_status_name_by_id(status_name: schemas.StatusName):
    query = f"update status_names set name = '{status_name.status_name}' where status_name_id = {status_name.status_name_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("status_names", status_name_id=status_name.status_name_id)





