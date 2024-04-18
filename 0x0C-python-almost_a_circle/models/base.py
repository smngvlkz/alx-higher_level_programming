#!/usr/bin/python3
import json
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
