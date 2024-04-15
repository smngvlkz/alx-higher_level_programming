#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class
    It inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of Rectangle

        Args:
            width: Width of the rectangle
            height: Heighr of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectanlge instance
        """
        return "<8-rectangle.Rectangle object at 0x7f6f488f7eb8>"

