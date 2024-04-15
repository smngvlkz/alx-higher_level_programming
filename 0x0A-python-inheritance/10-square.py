#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class
    Inherits from Rectangle.

    Attributes:
        _size: Size of the square
    """

    def __init__(self, size):
        """
        Initializes a new instance of square.

        Args:
            size: Square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns square area

        Returns:
            int: Square area.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns string representation of the square

        Returns:
            str: A string in the format '[Rectangle] <size>/<size>'.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
