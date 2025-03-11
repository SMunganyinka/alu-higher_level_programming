#!/usr/bin/python3
"""
This module provides a script that takes command-line arguments,
adds them to a Python list, and saves the updated list to a JSON file
named 'add_item.json'.

Functionality:
- Loads an existing JSON file containing a list (if available).
- Adds new command-line arguments to the list.
- Saves the updated list back to the JSON file.

Dependencies:
- `save_to_json_file` from `5-save_to_json_file.py`
- `load_from_json_file` from `6-load_from_json_file.py`

Usage:
    $ ./add_items_json.py arg1 arg2 arg3
"""

import sys
import os
from 5-save_to_json_file import save_to_json_file  # Function to save data as JSON
from 6-load_from_json_file import load_from_json_file  # Function to load data from JSON

FILENAME = "add_item.json"

def main():
    """Handles loading, updating, and saving the JSON list."""
    # Load existing data if the file exists, otherwise start with an empty list
    if os.path.exists(FILENAME):
        items = load_from_json_file(FILENAME)
        if not isinstance(items, list):  # Ensure data integrity
            items = []
    else:
        items = []

    # Append new arguments to the list (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(items, FILENAME)

if __name__ == "__main__":
    main()
