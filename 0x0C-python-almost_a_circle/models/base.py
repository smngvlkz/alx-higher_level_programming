#!/usr/bin/python3
import json
import os
"""
Base class Module.
"""
class Base:
    """
    Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of list_dictionaries returned.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        JSON string representation json_string returned.
        """
        if json_string is None or len(json_string) == 0:
            return[]
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string representation of list_obj to a file written.
        """
        filename = f"{cls.__name__}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as f:
            f.write(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Load instance from file.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all dictionary attribute already set.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise TypeError("Cannot create instance for this class name")
        dummy.update(**dictionary)
        return dummy
