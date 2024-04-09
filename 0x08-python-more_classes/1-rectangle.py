#!/usr/bin/python3
class Rectangle:
    """
    Defines a rectangle with private attributes for width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width: rectangle's width. defaults to 0.
            height: rectangle's height. also defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves private attributes width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of private attribute width.

        Raises:
            TypeError: value if not an integer.
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
        Retrieves private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets value for private attribute heught.

        Raises:
            TypeError: value if not an integer.
            ValueError: value if less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
