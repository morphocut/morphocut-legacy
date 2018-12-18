from sqlalchemy import Table, Column, ForeignKey, Index

import datetime

from sqlalchemy.types import Integer, BigInteger, String, DateTime, PickleType, Boolean, Text, Float
from sqlalchemy.sql.schema import UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql import func
from leadeagle.extensions import database

metadata = database.metadata

#: :type datasets: sqlalchemy.sql.schema.Table
datasets = Table('datasets', metadata,
    Column('dataset_id', Integer, primary_key=True),
    Column('name', String),
    Column('objects', Integer),
    Column('creation_date', DateTime,
        default=datetime.datetime.now),
)

#: :type objects: sqlalchemy.sql.schema.Table
objects = Table('objects', metadata,
    Column('object_id', Integer, primary_key=True),
    Column('filepath', String),
    Column('creation_date', DateTime,
        default=datetime.datetime.now),
    Column('dataset_id', Integer, ForeignKey('datasets.dataset_id'), index=True),
)
