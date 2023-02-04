from fastapi_sqlalchemy import db
from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import UserCreate


def create_user(user: UserCreate):
    query = f"insert into users (name) values ('{user.name}') RETURNING user_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("users", user_id=row['user_id'])


def update_user_by_id(user: schemas.User):
    query = f"update users set name = '{user.name}' where user_id = {user.user_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("users", user_id=user.user_id)





