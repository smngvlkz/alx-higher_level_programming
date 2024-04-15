#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from specified class.

    Args:
        obj: Object to check
        a_class: Class to check agaisnt.

    Returns:
        True if object is an instance of a class inherited from the
        specified class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
