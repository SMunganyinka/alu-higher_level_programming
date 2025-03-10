#!/usr/bin/python3
"""
Module for converting a JSON string representation to a Python object.

This module provides a function to deserialize a JSON-formatted string
into its corresponding Python data structure using `json.loads()`.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
