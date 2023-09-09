from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table


Base = declarative_base()

users = Table(
    "users",
    Base.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('age', Integer)
)
