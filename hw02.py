import datetime
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from sql_app import schemas
from sql_app.database import Base, engine, SQLALCHEMY_DATABASE_URL
from sql_app.cruds import users_crud, events_crud, bets_crud
from sql_app.schemas import UserCreate, BetCreate, EventCreate

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABASE_URL)


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


# Users
@app.get("/")
async def root():
    return "Use /users, /bets, /events endpoint to get data or /docs to open page with all endpoints"


@app.get("/init")
def init():
    return users_crud.init()


@app.get("/users")
def get_all_users():
    return users_crud.get_all_users()


@app.get("/users/{id}")
def get_user_by_id(id: int):
    return users_crud.get_user_by_id(id)


@app.post("/users")
def create_user(user: UserCreate):
    return users_crud.create_user(user)


@app.put("/users")
def update_user_by_id(user: schemas.User):
    return users_crud.update_user_by_id(user)


@app.delete("/users/{id}")
def delete_user_by_id(id: int):
    return users_crud.delete_user_by_id(id)


@app.delete("/users")
def delete_all_users():
    return users_crud.delete_all_users()


# Bets
@app.get("/bets")
def get_all_bets():
    return bets_crud.get_all_bets()


@app.get("/bets/{id}")
def get_bet_by_id(id: int):
    return bets_crud.get_bet_by_id(id)


@app.get("/bets/{user_id}")
def get_bets_by_user_id(user_id: int):
    return bets_crud.get_bets_by_user_id(user_id)


@app.post("/bets")
def create_bet(bet: BetCreate):
    return bets_crud.create_bet(bet)


@app.put("/bets")
def update_bet_by_id(bet: schemas.Bet):
    return bets_crud.update_bet_by_id(bet)


@app.delete("/bets/{id}")
def delete_bet_by_id(id: int):
    return bets_crud.delete_bet_by_id(id)


@app.delete("/bets")
def delete_all_bets():
    return bets_crud.delete_all_bets()


# Events

@app.get("/events")
def get_all_events():
    return events_crud.get_all_events()


@app.get("/events/{id}")
def get_event_by_id(id: int):
    return events_crud.get_event_by_id(id)


@app.post("/events")
def create_event(event: EventCreate):
    return events_crud.create_event(event)


@app.put("/events")
def update_event_by_id(event: schemas.Event):
    return events_crud.update_event_by_id(event)


@app.delete("/events/{id}")
def delete_event_by_id(id: int):
    return events_crud.delete_event_by_id(id)


@app.delete("/events")
def delete_all_events():
    return events_crud.delete_all_events()
