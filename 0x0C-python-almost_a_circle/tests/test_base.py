#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base

import os
import json

class TestBase(unittest.TestCase):
    """
    Base class test case.
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_id(self):
        """
        Class with no id provided.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_id(self):
        """
        Base class with id provided.
        """
        b1 = Base(8)
        b2 = Base()
        self.assertEqual(b1.id, 8)
        self.assertEqual(b2.id, 1)

    def test_to_json_string(self):
        """
        to_json_string static method test case.
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        list_dicts = [{'id': 1, 'size': 10, 'x': 2, 'y': 1}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, '[{"id": 1, "size": 10, "x": 2, "y": 1}]')

    def test_from_json_string(self):
        """
        from_json_string method test case.
        """
        json_str = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        expected_output = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(Base.from_json_string(json_str), expected_output)

        json_str = None
        expected_output = []
        self.assertEqual(Base.from_json_string(json_str), expected_output)

        json_str = ''
        expected_output = []
        self.assertEqual(Base.from_json_string(json_str), expected_output)

    def test_save_to_file(self):
        """
        save_to_file class method test case.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            list_objs = json.load(file)

        self.assertEqual(list_objs, [r1.to_dictionary(), r2.to_dictionary()])

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
if __name__ == "__main__":
    unittest.main()
