#!/usr/bin/python3
"""
Module: 7-add_item.py

This script adds all command-line arguments to a Python list and saves them to a file.

It utilizes the functions save_to_json_file and load_from_json_file from separate modules:
- save_to_json_file: Saves a Python object to a JSON file.
- load_from_json_file: Loads a Python object from a JSON file.

The list is stored in a JSON file named 'add_item.json'.
If the file does not exist, it is created.

Usage:
    ./7-add_item.py arg1 arg2 ...

Example:
    $ ./7-add_item.py Best School
    $ cat add_item.json
    ["Best", "School"]

    $ ./7-add_item.py 89 Python C
    $ cat add_item.json
    ["Best", "School", "89", "Python", "C"]
"""

import sys
import os
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file

FILENAME = "add_item.json"

def load_items(filename):
    """Load existing items from a JSON file or return an empty list if the file does not exist."""
    if os.path.exists(filename):
        return load_from_json_file(filename)
    return []

def save_items(filename, items):
    """Save the given list of items to a JSON file."""
    save_to_json_file(items, filename)

# Load existing items
items = load_items(FILENAME)

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_items(FILENAME, items)
