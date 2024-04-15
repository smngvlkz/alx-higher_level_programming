#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or an instance if a class
    that inherited from, the specified class.

    Args:
        obj: Object to check.
        a_class: Class to check against.

    Returns:
        True if object is an instance of, or an instance of a class that
        inherited from, specified class, otherwise False.
    """
    return isinstance(obj, a_class)
