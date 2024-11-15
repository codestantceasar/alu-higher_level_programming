#!/usr/bin/python3
"""
3-to_json_string.py

This module provides a function to convert a Python object to its JSON string

Functions:
    to_json_string(my_obj): Returns the JSON representation of a Python object as a string.
"""

import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string.

    Args:
        my_obj (Any): The Python object to convert to JSON.

    Returns:
        str: The JSON string representation of the input object.
    """
    return json.dumps(my_obj)
