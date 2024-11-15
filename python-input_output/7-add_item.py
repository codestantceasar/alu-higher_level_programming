#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list and saves them
to a file as a JSON representation. The file name is `add_item.json."""

import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load the existing list if the file exists, otherwise initialize an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Extend the list with new command-line arguments
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
