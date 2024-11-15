#!/usr/bin/python3
"""
0-read_file.py

This module provides a function to read a text file (UTF-8 encoded)
and print its contents to standard output.

Functions:
    read_file(filename=""): Reads and prints the content of the specified file.
"""


def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The path to the file to be read. """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
