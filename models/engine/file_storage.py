#!/usr/bin/python3
"""
Import python package models and other python packages
"""

import models
import os
from models.base_model import BaseModel
import json
from models.user import User
"""
class FileStorage: recreate a BaseModel from another one
by using a dictionary representation
"""


class FileStorage:
    """
    Create Private class attributes and
    Public instance methods
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.classes = []

    def all(self):
        """Returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
        Args:
            obj
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        serialized_objects = {
                key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                new_data = json.load(file)
                for key, value in new_data.items():
                    class_name, obj_id = key.split('.')
                    new_dict = globals()[class_name](**value)
                    self.__objects[key] = new_dict
        except FileNotFoundError:
            pass
