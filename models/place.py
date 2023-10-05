#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os
import models
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id", ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60), ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
    else:
        @property
        def reviews(self):
            """Returns instances of Review where place_id equals
            self.id.
            """

            reviews = [review for review in models.storage.all('Review').values()
                       if review.place_id == self.id]
            return reviews

        @property
        def amenities(self):
            """Returns many instances of Amenity based on Amenity.id.
            """

            amenities = [amenity for amenity in models.storage.all(
                'Amenity').values() if amenity.id in self.amenity_ids]

            return amenities

        @amenities.setter
        def amenities(self, value=None):
            """Adds ids in amenity_ids ."""
            if type(value) == type(Amenity):
                self.amenity_ids.append(value.id)


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))
