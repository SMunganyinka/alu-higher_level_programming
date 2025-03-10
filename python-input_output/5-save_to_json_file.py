#!/usr/bin/python3
"""
Module for saving an object to a file using a JSON representation.

This module provides a function to serialize a Python object into JSON format
and write it to a UTF-8 encoded text file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to be serialized and written to the file.
        filename (str): The name of the file where the JSON data will be saved.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
