#!/usr/bin/python3
"""Test case for Rectangle module."""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases"""

    def test_id_assignment(self):
        """Test id assignment in class."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validation(self):
        """Rectangle class test validation."""
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)
if __name__ == "__main__":
    unittest.main()
