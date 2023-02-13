import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:qwerty123@rds-instance-group-5.c2ncm6mxe8zp.eu-central-1.rds.amazonaws" \
                          ".com/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


def create_my_engine():
    my_engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    return my_engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
