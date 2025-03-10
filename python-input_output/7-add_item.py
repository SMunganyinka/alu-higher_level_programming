#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a file in JSON format.

This script first loads an existing list from a file named `add_item.json`
(if the file exists). It then appends all command-line arguments (excluding
the script name) to the list, and saves the updated list back to the same file.
If the file doesn't exist, it will create one and start with an empty list.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list from file if it exists, otherwise start with an empty list
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments (excluding script name)
my_list.extend(sys.argv[1:])

# Save updated list to the file
save_to_json_file(my_list, filename)
