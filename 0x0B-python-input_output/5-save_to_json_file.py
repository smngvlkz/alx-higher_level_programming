#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using JSON representation.

    Args:
        my_obj: Object to be converted to a JSON string and written to the file.
        filename: Name of the file to be written to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
