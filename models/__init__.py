
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

storage = FileStorage()
storage.reload()

classes = {
    'BaseModel': BaseModel,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}
