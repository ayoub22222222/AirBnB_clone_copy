#!/usr/bin/python3
"""This is the base models script """
import uuid
from datetime import datetime
import models


class BaseModel:
    """Class from which all other classes will inherit """

    def __init__(self, *args, **kwargs):
        """Initialization of the base model 
        args:
            - *args: list of arguments
            - **kwargs: dict of the key-values arguments
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
        """ update the public instance attribute update_at"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionnary containing all keys/values of __dict__"""

        new_one = self.__dict__.copy()
        new_one['__class__'] = self.__class__.__name__
        new_one['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_one['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return new_one

    def __str__(self):
        """ Returns official string representation"""

        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)

    def __repr__(self):
        """ Returns string representation of the result"""

        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))
