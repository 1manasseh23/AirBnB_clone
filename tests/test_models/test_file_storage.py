import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        result = self.storage.all()
        expected_result = {obj_key: {'id': obj.id, '__class__': 'BaseModel'}}
        self.assertEqual(result, expected_result)

    def test_new(self):
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        result = self.storage.all()
        self.assertEqual(result, {obj_key: obj})

    def test_save_reload(self):
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        result = new_storage.all()
        self.assertEqual(result, {obj_key: obj})

if __name__ == '__main__':
    unittest.main()

