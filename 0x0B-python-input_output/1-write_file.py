#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Args:
        filename: Name of the file to be written to. Defaults to an empty string.
        text: Text to be written to the file. Defaults to an empty string.

    Returns:
        int: Number of characters written to the file.

    Raises:
        IOError: the file if can't be opened for writing.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
