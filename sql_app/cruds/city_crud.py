from fastapi_sqlalchemy import db
from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import CityCreate


def create_city(city: CityCreate):
    query = f"insert into city (city_name, country_id) values ('{city.city_name}', '{city.country_id}') RETURNING city_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("city", city_id=row['city_id'])


def update_city_by_id(city: schemas.City):
    query = f"update city set city_name = '{city.city_name}', country_id = '{city.country_id}' where city_id = {city.city_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("city", city_id=city.city_id)





