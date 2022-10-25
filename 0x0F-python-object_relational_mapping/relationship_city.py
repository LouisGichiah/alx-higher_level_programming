#!/usr/bin/python3
"""
contains the class City
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
<<<<<<< HEAD
        """Represents a city for a MySQL database.
        Attributes:
            id (sqlalchemy.Column): The city's id.
            name (sqlalchemy.Column): The city's name.
            state_id (sqlalchemy.Column): The city's state id
        """
        __tablename__ = "cities"
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
=======
    """Representation of a city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
