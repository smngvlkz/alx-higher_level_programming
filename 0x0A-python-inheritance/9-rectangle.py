#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class inherits from BaseGeometry.

    Attributes:
        _width: Width of rectangle.
        _height: Heighr of the rectangle.
    """

    def __init__(self, width, height):
        """
        Intitializes a new instance of Rectangle.

        Args:
            width: Width of the rectangle
            height: Heighr of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns rectangle's area

        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format '[Rectangle] <width>/<height>'.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
