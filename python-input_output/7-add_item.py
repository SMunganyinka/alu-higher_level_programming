#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a file in JSON format.
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
