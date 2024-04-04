#!/usr/bin/python3
"""
Square module.

Defines square class that describes square by its size.
"""

class Square:
    """
    Defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes a new square object.

        Args:
            size (number, optional): square size. Defaults to 0.

        Raises:
            TypeError: size if not a number(float or integer).
            ValueError: size if less than 0.
        """

        if not isinstance(size, (int, float)):
            raise TypeError("soze must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """
        Getter for size attribute.

        Returns:
            number: current size of square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attributes.

        Args:
            value (number): new size for square.

        Rauses:
            TypeError: value if npt a number (flaot or integer)
            ValueError: value if less than 0.
        """

        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and return square area.

        Returns:
            float: square area.
        """

        return self.__size * self.__size

    def __eq__(self, other):
        """
        Equality comparison based on the square area.

        Args:
            bool: True if areas equal, Otherwise False.
        """

        if not isinstance(other, Square):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison based on square area.

        Args:
            other: (Square): square to compare with.

        Returns:
            bool: True if areas are not equal, otherwise False.
        """

        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Less than comparing based on square area.

        Args:
            other (Square): other square to compare with.

        Returns:
            bool: True if square area is less than other's, otherwise False.
        """

        if not isinstance(other, Square):
            return False
        return self.area() < other.area()
    
    def __le__(self, other):
        """
        Less than or equal comparison based on square area.

        Args:
            other (Square): other square to compare with.

        Returns:
            bool: True if current square's area is less than or equal to others,
            otherwise False.
        """

        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """
        Greater than comparison based on square area.

        Args:
            other (Square): other square to compare with.

        Returns:
            bool: True if current square area is greater than other,
            otherwise False.
        """

        return not (self.__lt__(other) or self.__eq__(other))

    def __ge__(self, other):
        """
        Greater than or equal comparison based on the square area.

        Args:
            other (Sqwuare): other square to compare with.

        Returns:
            bool: True if current square area is greater than or equal to others, otherwise False.
        """

        return self.__gt__(other) or self.__eq__(other)
