#!/usr/bin/python3
""" explain the purpose of the class """
import uuid
from datetime import datetime


class BaseModel:
    """description the class
    compenent
    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """ should print name of the class
        the id and dict """
        copy_dict = self.__dict__.copy()
        copy_dict.update(self.__class__.__dict__)
        comp_list = [
                '__module__', '__doc__', '__str__',
                '__dict__', 'to_dict', '__weakref__', 'save']
        filter_dict = {
                key: value for key,
                value in copy_dict.items() if key not in comp_list}
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, filter_dict)

    def save(self):
        """ update the public instance attribute update_at
        with the current date time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing key/value of __dict__ for an instance
        """
        comp_list1 = [
                '__module__', '__doc__', '__str__',
                '__dict__', 'to_dict', '__weakref__', 'save']
        new_ob = self.__dict__.copy()
        new_ob.update(self.__class__.__dict__)
        new_one = {
                key: value for key,
                value in new_ob.items() if key not in comp_list1}
        new_one['__class__'] = self.__class__.__name__
        new_one['updated_at'] = self.updated_at.isoformat()
        new_one['created_at'] = self.created_at.isoformat()
        return new_one
