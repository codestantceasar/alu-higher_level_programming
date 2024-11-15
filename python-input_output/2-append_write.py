#!/usr/bin/python3
"""
2-append_write.py

This module provides a function to append a string to a text file(UTF-8 encod)
and returns the number of characters added.

Functions:
    append_write(filename="", text=""): Appends text to the specified file.
"""
def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of characters added.
    Args:
        filename (str): The path to the file where the text will be appended.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        written = f.write(text)
    return written
