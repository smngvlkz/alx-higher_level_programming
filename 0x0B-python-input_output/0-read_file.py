#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file(UTF8) and prints it ti stdout.

    Args:
        filename: Name of the file to be read. Defaults to an empty
        string.

    Raises:
        FileNotFoundError: the file if it doesn't exist
        IOError: the file if can't be opened.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
