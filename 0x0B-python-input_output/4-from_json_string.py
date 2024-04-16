#!/usr/bin/python3
import json

def from_json_string(my_str):
    """
    Returns an object (Python data strucutre) represented by a JSON string.

    Args:
        my_str: JSON string to be converted to a Python object.

    Returns:
        object: Python object represented by `m_str`.

    Raises:
        ValueError: `my_str` if is not a valid JSON string.
    """
    return json.loads(my_str)
