#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a JSON file.
"""

import sys
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

FILENAME = "add_item.json"

# Load existing data if the file exists, otherwise start with an empty list
if os.path.exists(FILENAME):
    items = load_from_json_file(FILENAME)
else:
    items = []

# Append new arguments to the list (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, FILENAME)
