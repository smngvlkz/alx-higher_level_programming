#!/usr/bin/python3
"""
Square module.

Defines the Square class that describes a square position.
"""

class Square:
    """
    Defines a square by position and size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialzies a new square object

        Args:
            size (int, optional): size of sqaure. defaults to 0.
            postion (tuple, optional): square position.
                Defaults to (0, 0).

        Raises:
            TypeError:
                    - size if not an integer.
                    - position is not a tuple of 2 positive integers.
            ValueError: size if less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in position):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter for size attribute.

        Returns:
            int: current square size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): new square size.

        Raises:
            TypeError: value if not an integer
            ValueError: value if less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter for position attribute.

        Returns:
            tuple: current square position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute.

        Args:
            value (tuple): new square position

        Raises:
            TypeError:
                value if not a tuple of 2 positive integers.
            ValueError:
                any element in tuple if less than 0.
        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if any(i < 0 for i in value):
            raise ValueError("poisition must be a tuple of 2 positive integer")
        self.__position = value

        def area(self):
            """
            Calculates and returns square area.
            """

            return self.__size * self.__size

        def my_print(self):
            """
            Prints square representation using #

            if size is 0, prints empty line.
            """

            x, y = self.__position

            if self.__size == 0:
                print()
            else:
                for _ in range(y):
                    print()

                for _ in range(self.__size):
                    print(" " * x + "#" * self.__size)

