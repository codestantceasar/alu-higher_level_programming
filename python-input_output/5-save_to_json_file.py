#!/usr/bin/python3
"""
5-save_to_json_file.py

This module provides a function to write a Python object to a text file
using its JSON representation.

Functions:
    save_to_json_file(my_obj, filename): Writes a Python object to a file in JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj (Any): The Python object to serialize and write to the file.
        filename (str): The name of the file where the JSON representation will be stored.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
