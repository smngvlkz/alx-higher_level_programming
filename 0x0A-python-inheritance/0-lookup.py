#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: Object to inspect.

    Returns:
        Alist of names of the available attributes ad methods of `obj`.
    """
    return dir(obj)
