#!/usr/bin/python3
import sys
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: Object to be converted to a JSON string and written to the file.
        filename: Name of the file to be written to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))

def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    Args:
        filename: Name of the file to be read and converted to a Python object.

    Returns:
        object: Python object represented by the JSON string in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        file_contents = f.read()
        if file_contents:
            return json.loads(file_contents)
        else:
            return []

def main():
    """
    Main function that adds all arguments to a Python list, and then saves them to a file.

    tries to first load a list from `load_from_json_file`.
    if file doesn't exist, initializes an empty list.
    `add_item.json` using the function `save_to_json_file`.
    """
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, "add_item.json")

if __name__ == "__main__":
    main()
