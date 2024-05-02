#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This is the class for user
    """

    __tablename__ = "users"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user', cascade='delete')
        reviews = relationship('Review', backref='user', cascade='delete')