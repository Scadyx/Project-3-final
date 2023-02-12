from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def get(db: Session, table: str, **args):
    query = get_query(table, **args)
    print(query)
    print(text("select * " + query))
    result = db.execute(text("select * " + query)).fetchall()
    # rows = []
    # for row in result:
    #     rows.append(row)
    print(result)
    return result


def delete(db: Session, table: str, **args):
    query = get_query(table, args)
    try:
        db.execute(text("delete " + query))
        db.commit()
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
