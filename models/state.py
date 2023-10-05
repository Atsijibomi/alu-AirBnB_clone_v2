#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models import FileStorage, DBStorage, storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if isinstance(storage, DBStorage):
        cities = relationship('City', back_populates="State",
                              cascade="all, delete, delete-orphan")
    if isinstance(storage, FileStorage):
        @property
        def cities(self):
            """ Returns the list of City instances with state_id
            equals to the current State.id. """
            return [city for city in models.storage.all('City').values()
                    if city.state_id == self.id]
