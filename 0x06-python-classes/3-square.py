#!/usr/bin/python3
"""
Square module.

It defines the Square class that describes a square.
"""

class Square:
    """
    Defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int, optional): size of the square.
            Default to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueEror("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: area of the square.
        """

        return self.__size * self.__size
