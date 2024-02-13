#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel: Defines all common attributes and methods

    Args:
        *args:
        **kwargs:
    """

    def __init__(self, *args, **kwargs):
        """
        Initialiaze and instantiate public class attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        __str__ should print id and __dict__
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,self.id, str(self.__dict__))

    def save(self):
        """
        Save: Updates the public instance attribute
        updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        to_dict: Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        my_obj = self.__dict__.copy()
        my_obj["__class__"] = self.__class__.__name__
        my_obj["created_at"] = self.created_at.isoformat()
        my_obj["updated_at"] = self.updated_at.isoformat()
        return my_obj
