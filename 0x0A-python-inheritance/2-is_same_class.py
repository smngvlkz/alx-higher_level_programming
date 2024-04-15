#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: Object to check.
        a_class: Class to check against.

    Returns:
        True if object is exactly an instance of specified class, otherwise False.
    """
    return type(obj) is a_class
