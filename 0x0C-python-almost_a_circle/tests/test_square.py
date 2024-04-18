#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Test case for square class.
    """

    def test_initialization(self):
        """
        Initialization with and without.
        """
        s1 = Square(5, id=6)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(2, 4, 6, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 4)
        self.assertEqual(s2.y, 6)

    def test_size_setter(self):
        """
        Size setter.
        """
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

        with self.assertRaises(TypeError):
            s.size = "9"

    def test_validation(self):
        """
        Value validation in setters.
        """
        with self.assertRaises(TypeError):
            s = Square("10")

        with self.assertRaises(ValueError):
            s = Square(-2)

        with self.assertRaises(ValueError):
            s = Square(10, x=-1)

    def test_area(self):
        """
        Area calculation
        """
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """
        Overridden __str__ test case.
        """
        s1 = Square(4, 2, 1, 12)
        expected_str = f"[Square] ({s1.id}) {s1.x}/{s1.y} - {s1.width}"
        self.assertEqual(str(s1), expected_str)

        s2 = Square(5, 1)
        expected_str = f"[Square] ({s2.id}) {s2.x}/{s2.y} - {s2.width}"
        self.assertEqual(str(s2), expected_str)

    def test_update(self):
        """
        Update method test case.
        """
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

        s.update(1, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)

        s.update(1, 2, 3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)

        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

        s.update(x=12)
        self.assertEqual(s.x, 12)

        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

        s.update(size=7, id=89, y=1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

if __name__ == "__main__":
    unittest.main()
