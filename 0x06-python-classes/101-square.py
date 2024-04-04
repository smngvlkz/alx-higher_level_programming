#!/usr/bin/python3
"""
Square module.

Defines the Square class that describes a square position.
"""

class Square:
    """
    Defines the size and position of the square.
    """

    def __init__(self, size=0, position=(0,0)):
        """
        Initializes a ndw square object.

        Args:
            size (int, optional): size of the square. Defaults to 0.
            position (tuple, optional): position of square.
                Defaults to (0, 0).

        Raises:
            TypeError:
                - size if not an integer.
                - position if not a tuple of 2 positive integers.
            ValueError:
                - size if less than 0.
                - any element in tuple is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be tuple of 2 positive integers")
        if any(i < 0 for i in position):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: current size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): new size of square.

        Raises:
            TypeError: value if not an integr.
            VakueError: value if less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter for position attribute.

        Returns:
            tuple: current position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute.

        Args:
            value (tuple): new position for square.

        Raises:
            TypeError:
                value if not a tuple of 2 positive integers.
            ValueError:
                any element in tuple if less than 0.
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 posisitve integers")
        if any(i < 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calcute and returns square area.

        Returns:
            int: square area.
        """

        return self.__size * self.__size

    def __str__(self):
        """
        String representation of square object

        Returns:
            str: string of square with '#'.
        """

        x, y = self.__position

        if self.__size == 0:
            return ""

        output = " " * x + ("#" * self.__size + "\n") * self.__size
        return output[:-1]
