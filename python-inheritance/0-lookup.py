#!/usr/bin/python3
"""
This module defines a function `lookup` that returns a list of available
attributes and methods of a given object.

The function is useful for introspection, allowing users to inspect an object's
attributes and methods without importing any external modules.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    list: A list of attribute and method names available in the object.
    """
    return dir(obj)
