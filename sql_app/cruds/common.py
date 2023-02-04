from fastapi_sqlalchemy import db
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError


def get(table: str, **args):
    result = db.session.execute(text("select * " + get_query(table, **args)))
    rows = []
    for row in result:
        rows.append(row)
    return rows


def delete(table: str, **args):
    try:
        db.session.execute(text("delete " + get_query(table, **args)))
        db.session.commit()
    except IntegrityError:
        return {"error": "failed to delete"}


def get_query(table: str, **args):
    query = f"from {table}"
    if args.items():
        filters = []
        for key, value in args.items():
            filters.append(f"{key} = {value}")
        query = f"{query} where {' and '.join(filters)}"
    return query