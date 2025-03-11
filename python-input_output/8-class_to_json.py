#!/usr/bin/python3
"""
Module: class_to_json

This module provides a function to return the dictionary description
with a simple data structure for JSON serialization of an object.

Function:
- class_to_json: Converts an object's attributes into a dictionary
  suitable for JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: Dictionary representation of the object's attributes.
    """
    return obj.__dict__
