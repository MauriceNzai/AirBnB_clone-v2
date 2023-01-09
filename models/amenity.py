#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


<<<<<<< HEAD
class Amenity(BaseModel, Base)
=======
class Amenity(BaseModel, Base):
>>>>>>> 9880d03592d7bf9187a679576411c793782e2575
    """
    Amenity class, Models an amenity
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
