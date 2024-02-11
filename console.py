#!/usr/bin/python3
"""
Create class HBNBCommand
"""
import models
from models import storage
from models.base_model import BaseModel
import cmd
from models.user import User


"""
class HBNBCommand: Write a program called console.py that contains
the entry point of the command interpreter
Args:
    cmd.Cmd
"""

class HBNBCommand(cmd.Cmd):
    """
    Write prompt that creates entry point
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_create(self, arg):
        """
         Creates a new instance of BaseModel,
         saves it (to the JSON file) and prints the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)
        """
        pass

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        """
        if instance_id < 2:
            print("** instance id missing **")
            return
        """
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            instance_id = args[1]
            instance = BaseModel.get(instance_id)
            print(instance)
        except Exception:
            print("** no instance found **")
        """
        pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            instance_id = args[1]
            instance = BaseModel.get(instance_id)
            instance.delete()
        except Exception:
            print("** no instance found **")
        """
        pass

    """
    def do_all(self, arg):
        args = arg.split()
        if args and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        instances = BaseModel.all()
        print([str(instance) for instance in instances])
    """

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)
        """
        args = arg.split()
        if len(args) == 0:
            instances = storage.all()
        elif args[0] in models.classes:
            instances = storage.all(args[0])
        else:
            print("** class doesn't exist **")
            return

        for obj_id, obj in instances.items():
            print(obj)
        """
        pass

    def do_quit(self, arg):
        """
        To exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        To exit the program
        """
        print("\nGoodbye!")
        return True

    def emptyline(self):
        """
        shouldn’t execute anything
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.classes[class_name]()
        new_instance.save()
        print(new_instance.id)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            instance_id = args[1]
            instance = BaseModel.get(instance_id)
            if len(args) < 4:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(instance, attr_name, attr_value)
            instance.save()
        except Exception:
            print("** no instance found **")
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
