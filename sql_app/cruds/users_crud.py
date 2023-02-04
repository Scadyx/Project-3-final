import json
from fastapi_sqlalchemy import db
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from sql_app import schemas
from sql_app.schemas import UserCreate




def get_all_users():
    result = db.session.execute(text("select * from users"))
    users = []
    for row in result:
        users.append(row)
    return users


def get_user_by_id(id: int):
    result = db.session.execute(text("select * from users where id=" + str(id)))
    for row in result:
        return row


def create_user(user: UserCreate):
    query = f"insert into users (name, last_name, balance, ip, age, gender, time_created, premium, birth_day, city) " \
            f"values ('{user.name}', '{user.last_name}', '{user.balance}', '{user.ip}', '{user.age}', '{user.gender}'" \
            f", '{user.time_created}', '{user.premium}', '{user.birth_day}', '{user.city}') RETURNING id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return get_user_by_id(row['id'])


def update_user_by_id(user: schemas.User):
    query = f"update users set name = '{user.name}', last_name = '{user.last_name}', balance = '{user.balance}', " \
            f"ip = '{user.ip}', age = '{user.age}', gender = '{user.gender}', time_created = '{user.time_created}', " \
            f"premium = '{user.premium}', birth_day = '{user.birth_day}', city = '{user.city}' where id = {user.id}"
    db.session.execute(text(query))
    db.session.commit()
    return get_user_by_id(user.id)


def delete_user_by_id(id: int):
    try:
        db.session.execute(text("delete from users where id=" + str(id)))
        db.session.commit()
        return "OK"
    except IntegrityError:
        return {"error": "user is linked to bet"}


def delete_all_users():
    try:
        db.session.execute(text("delete from users"))
        db.session.commit()
    except IntegrityError:
        return {"error": "users are linked to bets"}
