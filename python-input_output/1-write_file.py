#!/usr/bin/python3
"""
1-write_file.py

This module provides a function to write a string to a text file (UTF-8 encoded)
and returns the number of characters written.

Functions:
    write_file(filename="", text=""): Writes text to the specified file.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written.

    Args:
        filename (str): The path to the file where the text will be written.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        written = f.write(text)
    return written

