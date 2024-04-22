#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

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

    def test_load_from_file(self):
        """
        test case for load_from_file method.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_input), len(list_rectangles_output))
        for r_in, r_out in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(r_in), str(r_out))
        
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(len(list_squares_input), len(list_squares_output))
        for s_in, s_out in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(s_in), str(s_out))

    def test_create(self):
        """
        Create method test case.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_save_load_from_file_csv(self):
        """
        save_to_file_cvs and load_from_file_csv methods test case.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles_input), len(list_rectangles_output))
        for r_in, r_out in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(r_in), str(r_out))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(len(list_squares_input), len(list_squares_output))
        for s_in, s_out in zip(list_squares_input, list_squares_output):
            self.assertEqual(str(s_in), str(s_out))

    def test_draw(self):
        """
        Test case for draw static method.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares = [s1, s2]

        try:
            Base.draw(list_rectangles, list_squares)
        except Exception as e:
            self.fail(f"Test failed with exception: {e}")


if __name__ == "__main__":
    unittest.main()
