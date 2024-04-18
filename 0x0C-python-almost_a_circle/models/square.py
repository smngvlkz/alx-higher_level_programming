#!/usr/bin/python3
"""
Square class module.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Size getter.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Size setter.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        String representation for Square class.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
