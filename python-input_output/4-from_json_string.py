#!/usr/bin/python3
"""
4-from_json_string.py

This module provides a function to convert a JSON string to its corresponding
Python data structure.

Functions:
    from_json_string(my_str): Returns the Python object represented by a JSON .
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): A string representing a JSON object.

    Returns:
        Any: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
