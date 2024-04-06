#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Testing for max_integer function
    """
    def test_max_integer(self):
        """
        Lists of positive numbers to test with max_integer.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

    def test_max_integer_negative(self):
        """
        Lists of negative numbers to test with max_integer.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_max_integer_mixed(self):
        """
        Lists of mixed positivee and negative numbers to test with max_integer.
        """
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -3, 4, -2]), 4)

if __name__ == '__main__':
    unittest.main()
