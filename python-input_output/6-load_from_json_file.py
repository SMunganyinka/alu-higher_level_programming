#!/usr/bin/python3
"""
Module for loading an object from a JSON file.

This module provides a function to read a JSON-formatted file and
convert it into its corresponding Python data structure using `json.load()`.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
