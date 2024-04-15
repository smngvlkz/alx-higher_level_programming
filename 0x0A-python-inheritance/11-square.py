#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class inherits from Rectangle

    Attributes:
        _size: Square size
    """

    def __init__(self, size):
        """
        Initializes a new instance of Square.

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
            int: Square area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format '[Square] <size>/<size>'.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
