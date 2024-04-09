#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle with private attributes for width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new object.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
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

        Raises:
            TypeError: value if not an integer
            ValueError: value if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves private attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets value of private attribute height.

        Raises:
            TypeError: value if not an integer
            ValueError: value if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns rectangle's perimeter.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns perimeter of the rectangle.

        Cases where width or height is 0 will be handled"
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns representation string of rectangle using # characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width) + "\n") * self.__height

    def __repr__(self):
        """
        Returns representation string of the objec for recreation.
        """
        return f"Rectangle({self.width}, {self.height})"

