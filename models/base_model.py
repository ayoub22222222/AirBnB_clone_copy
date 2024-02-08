#!/usr/bin/python3
""" explain the purpose of the class """


class BaseModel:
    """description the class 
    compenent
    """
    def __init__(self):
        self.id = id
        self.created_at = #assigned with the current date time
        self.updated_at = #assign with the current datetime when an instance is created

    def __str__(self):
        """ should print name of the class
        the id and dict """
        pass
    def save(self):
        """ update the public instance attribute update_at
        with the current date time """
        pass
    def to_dict(self):
        """ return a dict ontaining all keys/values of 
        __dict__ of the instance"""
        pass


