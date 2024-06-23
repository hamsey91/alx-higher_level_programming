#!/usr/bin/python3
"""Contains the class definition of a State and an instance Base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata


class State(Base):
    """Represents a state class with id and attribute"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=Falsei)
