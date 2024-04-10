#!/usr/bin/python3
class LockedClass:
    """
    Only allows setting the first_name attribute.

    Uses the slots magic sttribute to lock class and prevent
    dynamic creation of attributes.

    Attributes:
        first_name: string for the frist name of the instance.
    """
    __slots__ = ['first_name']

