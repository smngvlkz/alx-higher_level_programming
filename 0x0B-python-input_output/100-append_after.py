#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text ti a file, after each line cintaining a specific string.

    Args:
        filename: Name of the file.
        search_string: String to be searched for.
        new_string: New string to be inserted after each line containing the search string.
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string
        f.seek(0)
        f.writelines(lines)
