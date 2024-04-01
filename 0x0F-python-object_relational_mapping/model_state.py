#!/usr/bin/python3
"""takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """state class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(120), nullable=False)
