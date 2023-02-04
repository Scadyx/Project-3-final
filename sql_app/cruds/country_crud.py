from fastapi_sqlalchemy import db
from sqlalchemy import text
from sql_app import schemas
from sql_app.cruds import common
from sql_app.schemas import CountryCreate


def create_country(country: CountryCreate):
    query = f"insert into country (country_name) values ('{country.country_name}') RETURNING country_id"
    result = db.session.execute(text(query))
    db.session.commit()
    for row in result:
        return common.get("country", country_id=row['country_id'])


def update_country_by_id(country: schemas.Country):
    query = f"update country set name = '{country.country_name}' where country_id = {country.country_id}"
    db.session.execute(text(query))
    db.session.commit()
    return common.get("country", country_id=country.country_id)





