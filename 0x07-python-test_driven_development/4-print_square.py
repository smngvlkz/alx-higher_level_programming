#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with a character #.

    Args:
        size (int): size length of the square.

    Raises:
        TypeError: size if not an integer, or is a float and less than 0.
        ValueError: size if less than 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
