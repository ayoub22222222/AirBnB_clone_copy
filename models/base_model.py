#!/usr/bin/python3
""" explain the purpose of the class """
import uuid
from datetime import datetime


class BaseModel:
    """description the class 
    compenent
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """ should print name of the class
        the id and dict """
        return "[{:s}] ({:s}) {:s}".format(BaseModel.__name__, str(self.id), str(self.__dict__))
        

    def save(self):
        """ update the public instance attribute update_at
        with the current date time """
        self.updated_at = datetime.now().isoformat()
        

    def to_dict(self):
        """ return a dict ontaining all keys/values of 
        __dict__ of the instance"""
        return self.__dict__

