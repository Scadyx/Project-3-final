from fastapi_sqlalchemy import db
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from sql_app import schemas
from sql_app.schemas import EventCreate


def get_all_events():
    result = db.session.execute(text("select * from events"))
    events = []
    for row in result:
        events.append(row)
    return events


def get_event_by_id(id: int):
    result = db.session.execute(text("select * from events where id=" + str(id)))
    for row in result:
        return row


def create_event(event: EventCreate):
    query = f"insert into events (event_date, name, type) " \
            f"values ('{event.event_date}', '{event.name}', '{event.type}') RETURNING id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return get_event_by_id(row['id'])


def update_event_by_id(event: schemas.Event):
    query = f"update events set event_date = '{event.event_date}', type = '{event.type}', name = '{event.name}'" \
            f" where id = {event.id}"
    db.session.execute(text(query))
    db.session.commit()
    return get_event_by_id(event.id)


def delete_event_by_id(id: int):
    try:
        db.session.execute(text("delete from events where id=" + str(id)))
        db.session.commit()
        return "OK"
    except IntegrityError:
        return {"error": "event is linked to bet"}


def delete_all_events():
    try:
        db.session.execute(text("delete from events"))
        db.session.commit()
    except IntegrityError:
        return {"error": "events are still linked to bets"}
