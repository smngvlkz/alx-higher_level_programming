#!/usr/bin/python3
"""
Contains the class definition of a State and connects to a MySQL database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class linked to states table in MySQL database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
