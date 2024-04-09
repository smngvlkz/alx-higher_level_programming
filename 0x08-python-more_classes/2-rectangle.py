#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle with private attributes for width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initialzies a new object

        Args:
            width: Rectangle's width.
            height: Rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves private attribute width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets value of private attribute width.

        Raiases:
            TypeError: value if is not an integer.
            ValueError: value if less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves value of private attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets value of private attribute height.

        Raises:
            TypeError: value if not an integer.
            ValueError: value if less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates an returns area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns perimeter of rectangle

        Cases where width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
