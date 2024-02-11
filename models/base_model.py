#!/usr/bin/python3
"""This is the base models script """
import uuid
from datetime import datetime
import models


class BaseModel:
    """Class from which all other classes will inherit """

    def __init__(self, *args, **kwargs):
        """this class is about to bla
        bla and it conatin tree instance
        attribute
        args:
            param: str id
            param2: ctreated_at time
            parame3: updated_at time
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for i, j in kwargs.items():
                if "__class__" not in i:
                    setattr(self, i, j)

    def save(self):
        """ update the public instance attribute update_at
        with the current date time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing key/value of __dict__ for an instance
        """
        new_one = self.__dict__.copy()
        new_one['__class__'] = self.__class__.__name__
        new_one['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_one['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return new_one

    def __str__(self):
        """ should print name of the class
        the id and dict """
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)

    def __repr__(self):
        """ string representation of the
        the result"""
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))
