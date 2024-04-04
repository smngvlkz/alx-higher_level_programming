#!/usr/bin/python3
"""
Square module.

Defines square class that describes a square.
"""

class Square:
    """
    Defines a square
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int, optional): Size of the square.

        Raises:
            TypeError: size is not integer.
            ValueError: size is less than 0.
        """

        self.__size = size

        @property
        def size(self):
            """
            Getter for size attribute.

            Returns:
                int: current size of square.
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            Setter for size attribute

            Args:
                value (int): new square size.

            Raises:
                TypeError: value is not an integer
                ValueError: value less than 0.
            """

            if not isinstance(value, int):
                raise TypeError("size must be integer")
            if value < 0:
                raise ValueError("size must be >= 0")

            self.__size = value

        def area(self):
            """
            Calculate and returns the area of the square..

            Returns:
                int: The square area.
            """

            return self.__size * self.__size

