#!/usr/bin/python3
"""
Defines a function that returns the dictionary description
for JSON serialization of an object.
"""

def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing all attributes of the object.
    """
    return obj.__dict__
