#!/usr/bin/python3
def text_indentation(text):
    """
    Indents a text withh 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): Indented text.

    Raises:
        TypeError: text if not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    lines = text.split("\n")
    for i, line in enumerate(lines):
        lines[i] = line.strip()
    text = "\n".join(lines)
    print(text)
