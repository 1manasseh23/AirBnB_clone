#!/usr/bin/python3

import models
import os
from models.base_model import BaseModel
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        # for key, value in self.__objects.items():
            # serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                if os.stat(self.__file_path).st_size == 0:
                    return
                loaded_objects = json.load(file)
                for  key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    module_name = class_name.lower()
                try:
                    module = __import__(module_name)
                    class_ = getattr(module, class_name)
                    instance = class_(**value)
                    self.__objects[key] = instance
                except (ImportError, AttributeError) as e:
                    print(f"Error importing {module_name}.{class_name}: {e}")
                    """
                    module = __import__("models." + class_name, fromlist=[class_name])
                    obj = getattr(module, class_name)(**value)
                    # class_obj = globals()[class_name]
                    # self.__objects[key] = class_obj(**value)
                    self.__objects[key] = obj
                    """
        except FileNotFoundError:
            pass
