#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    Args:
        filename: Name of the file to be read and converted to a Python object.

    Returns:
        object: Python object represented by the JSON string in the file.

    Raises:
        FileNotFoundError: the file if it doesn't exist.
        IOError: the file if it can't be opened for reading.
        ValueError: the file if content is not valid JSON string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
