#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attr(self):
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_id(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertEqual(len(self.base_model.id), 36)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        new_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), new_str)

    def test_save(self):
        my_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(my_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()

        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())
    def test_deserialize(self):
        obj_dict = self.base_model.to_dict()
        new_model = BaseModel(**obj_dict)

        self.assertEqual(self.base_model.id, new_model.id)
        self.assertEqual(self.base_model.created_at, new_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_model.updated_at)

    def test_deserialize_extra_attr(self):
        obj_dict = self.base_model.to_dict()
        obj_dict['extra_attribute'] = 'extra value'

        with self.assertRaises(TypeError):
            new_model = BaseModel(**obj_dict)


if __name__ == "main":
    unittest.main()
