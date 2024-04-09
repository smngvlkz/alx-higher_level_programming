#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrives height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns represantation string for rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a represantation string of the rectangle in production.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when rectangle is deleted.
        """
        print("Bye rectangle...")
