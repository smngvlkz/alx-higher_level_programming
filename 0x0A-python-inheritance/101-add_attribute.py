#!/usr/bin/python3
def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if its possible

    Args:
        obj: Object to add attribute to
        attr: Name of the attribute
        value: Value of the attribute

    Raises:
        TypeError: Object if it can't havre a new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
