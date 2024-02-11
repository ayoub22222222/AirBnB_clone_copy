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
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ should print name of the class
        the id and dict """
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)

    def save(self):
        """ update the public instance attribute update_at
        with the current date time """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        Returns a dictionary containing key/value of __dict__ for an instance
        """
        new_one = self.__dict__.copy()
        new_one['__class__'] = self.__class__.__name__
        new_one['updated_at'] = self.updated_at.isoformat()
        new_one['created_at'] = self.created_at.isoformat()
        return new_one
