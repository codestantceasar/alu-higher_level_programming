#!/usr/bin/python3
 This module provides a function to read a text file (UTF-8 encoded)
and print its contents to standard output.

Functions:
    read_file(filename=""): Reads and prints the content of the specified file.
"""

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
