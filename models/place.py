#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    """
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, back_populates='place_amenities')
    
        @property
        def reviews(self):
            """returns the list of Review instances with
            place_id equals to the current Place.id
            """
            review_list = []
            rev_list = models.storage.all(Review).values()
            for revs in rev_list:
                if revs.place_id == self.id:
                    review_list.append(revs)
            return review_list

        @property
        def amenities(self):
            """returns the list of Amenities instances with
            Place.amenities
            """
            amenities_list = []
            rev_list = models.storage.all(models.amenity.Amenity).values()
            for revs in rev_list:
                if revs.place_id == self.id:
                    amenities_list.append(revs)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """...
            """
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)