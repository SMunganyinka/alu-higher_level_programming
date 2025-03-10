#!/usr/bin/python3
"""
Module for converting an object to its JSON string representation.

This module provides a function to serialize an object into a JSON-formatted
string.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON string representation of the object.
    """
    return str(my_obj).replace("'", '"')  # This is a simple workaround.
