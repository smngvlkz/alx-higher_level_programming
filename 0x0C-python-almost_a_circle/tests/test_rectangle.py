#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Rectangle class test case.
    """

    def test_initialization(self):
        """
        Initialization with and without.
        """
        r1 = Rectangle(10, 2, id=6)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 1, 4, 6, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 6)

    def test_validation(self):
        """
        Value validation in setters
        """
        with self.assertRaises(TypeError):
            r = Rectangle("10", 2)

        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, x=-1)

    def test_area(self):
        """
        Area calculation.
        """
        r = Rectangle(5, 3)
        self.assertEqual(r.area(), 15)

    def test_display(self):
        """
        Display method test case.
        """
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        expected_output2 = " ###\n ###\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output2)

    def test_str(self):
        """
        Overridden __str__ test case method.
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_str = f"[Rectangle] ({r1.id}) {r1.x}/{r1.y} - {r1.width}/{r1.height}"
        self.assertEqual(str(r1), expected_str)

        r2 = Rectangle(5, 5, 1)
        expected_str = f"[Rectangle] ({r2.id}) {r2.x}/{r2.y} - {r2.width}/{r2.height}"
        self.assertEqual(str(r2), expected_str)

if __name__ == "__main__":
    unittest.main()
