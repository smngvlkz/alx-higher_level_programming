#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization of an object.

    Args:
        obj: Object to be converted to a dictionary.

    Returns:
        dict: Dictionary representation of `obj`.
    """
    return vars(obj)
