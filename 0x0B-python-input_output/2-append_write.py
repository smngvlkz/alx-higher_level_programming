#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename: Name of the file to be written to. Defaults to an empty string.
        text: Text to be appended to the file. Defaults to an empty string.

    Returns:
        int: Number of characters added to the file.

    Raises:
        IOError: the file if can't be opened for writing.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
