#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Base class test case.
    """

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
        self.assertEqual(b2.id, 3)

if __name__ == "__main__":
    unittest.main()
