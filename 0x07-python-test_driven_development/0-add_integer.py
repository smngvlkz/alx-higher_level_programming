#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two numbers together.
    Takes two arguments, a and b, which should be integers or floats.
    if either is not an integer or float, it raises a TypeError.
    if arguments are floats, they casted into integers
    Returns: sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
