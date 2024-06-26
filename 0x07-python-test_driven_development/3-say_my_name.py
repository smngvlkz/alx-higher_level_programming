#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints My na,e is <first name> <last name>

    Args:
        first_name (str): First name to print.
        last_name (str, optional): Last name to print.
        Defaults to "".

    Raises:
        TypeError: either first_name or last_name if not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
