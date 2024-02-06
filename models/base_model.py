#!/usr/bin/python3
# Write a class BaseModel that defines all common attributes/methods for other classes
from uuid import uuid4
from datetime import datetime

"""class BaseModel that defines all common attributes/methods"""
class BaseModel:

    """Initialiaze and instantiate public class attributes"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    """__str__ should print id and __dict__"""
    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
    
    """updates the public instance attribute updated_at with the current datetime"""
    def save(self):
        self.updated_at = datetime.now()

    """Returns a dictionary containing all keys/values of __dict__ of the instance"""
    def to_dict(self):
        my_obj = self.__dict__.copy()
        my_obj["__class__"] = self.__class__.__name__
        my_obj["created_at"] = self.created_at.isoformat()
        my_obj["updated_at"] = self.updated_at.isoformat()
        return my_obj