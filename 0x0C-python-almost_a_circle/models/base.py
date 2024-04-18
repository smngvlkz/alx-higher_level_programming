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
