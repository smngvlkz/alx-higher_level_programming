#!/usr/bin/python3
"""
Square module.

Defines Square class that describes a square.
"""

class Square:
    """
    Defines a square size.
    """

    def __init__(self, size=0):
        """
        Intializes a new Square object.

        Args:
            size (int, optianal): Size of square. Default to 0.

        Raises:
            TypeError: size is not an integer.
            ValueError: size is less then 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
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
        Setter for size attribute.

        Args:
            value (int): new size for square.

        Raises:
            TypeError: value if not an integer
            ValueError: value if less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns are of square.

        Returns:
            int: area of square.
        """

        return self.__size * self.__size

    def my_print(self):
        """
        Prints square using #.

        if size is 0, prints empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
