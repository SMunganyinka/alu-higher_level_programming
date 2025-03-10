#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list and saves them to a file
in JSON format.

This script does the following:
1. Checks if a file named 'add_item.json' exists.
2. If the file exists, loads its contents into a Python list.
3. If the file does not exist, initializes an empty list.
4. Appends all command-line arguments (excluding the script name) to the list.
5. Saves the updated list back to 'add_item.json' as a JSON representation.

The file is created if it doesn't exist, and its content is updated if it already exists.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_arguments_to_json_file():
    """
    Adds all command-line arguments to a Python list and saves them to a file.

    This function performs the following steps:
    1. Checks if the file 'add_item.json' exists.
    2. If the file exists, loads its current contents into a list.
    3. If the file doesn't exist, initializes an empty list.
    4. Appends all command-line arguments (except the script name) to the list.
    5. Saves the updated list back to the file 'add_item.json' as a JSON representation.
    """
    filename = "add_item.json"

    # Check if the file 'add_item.json' exists
    if exists(filename):
        # If the file exists, load the current list from the file
        my_list = load_from_json_file(filename)
    else:
        # If the file doesn't exist, create an empty list
        my_list = []

    # Extend the list with command-line arguments (excluding the script name)
    my_list.extend(sys.argv[1:])

    # Save the updated list back to the file as a JSON representation
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    """
    The main entry point of the script.
    
    This section will execute the function to add command-line arguments
    to the list and save them to the JSON file.
    """
    add_arguments_to_json_file()
