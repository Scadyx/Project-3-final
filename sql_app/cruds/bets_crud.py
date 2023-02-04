from fastapi_sqlalchemy import db
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from sql_app import schemas

from sql_app.schemas import BetCreate


def get_all_bets():
    result = db.session.execute(text("select * from bets"))
    bets = []
    for row in result:
        bets.append(row)
    return bets


def get_bet_by_id(id: int):
    result = db.session.execute(text("select * from bets where id=" + str(id)))
    for row in result:
        return row


def get_bets_by_user_id(user_id: int):
    result = db.session.execute(text("select * from bets where user_id=" + str(user_id)))
    for row in result:
        return row


def create_bet(bet: BetCreate):
    try:
        query = f"insert into bets (date_created, user_id, event_id) " \
                f"values ('{bet.date_created}', '{bet.user_id}', '{bet.event_id}') RETURNING id"
        result = db.session.execute(text(query))
        db.session.commit()
        for row in result:
            return get_bet_by_id(row['id'])
    except IntegrityError:
        return {"error": "check provided user_id and event_id"}
    except:
        return {"error": "DB error"}


def update_bet_by_id(bet: schemas.Bet):
    try:
        query = f"update bets set user_id = '{bet.user_id}', event_id = '{bet.event_id}', date_created = '{bet.date_created}' " \
                f" where id = {bet.id}"
        db.session.execute(text(query))
        db.session.commit()
        return get_bet_by_id(bet.id)
    except IntegrityError:
        return {"error": "check provided user_id and event_id"}
    except:
        return {"error": "DB error"}


def delete_bet_by_id(id: int):
    db.session.execute(text("delete from bets where id=" + str(id)))
    db.session.commit()
    return "OK"


def delete_all_bets():
    db.session.execute(text("delete from bets"))
    db.session.commit()
