#!/usr/bin/python3
"""
Module 6-load_from_json_file

This module provides a function to create a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file to be read.

    Returns:
        object: The Python object created from the JSON file.

    Example:
        If the JSON file contains:
        ```
        {
            "name": "John",
            "age": 30,
            "is_active": true
        }
        ```
        Calling `load_from_json_file("file.json")` will return:
        {
            "name": "John",
            "age": 30,
            "is_active": True
        }

    Note:
        - This function assumes the JSON file exists and is properly formatted.
        - No exception handling for file permissions or invalid JSON format.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
