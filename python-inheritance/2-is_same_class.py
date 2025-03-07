#!/usr/bin/python3
"""
Module: is_same_class
----------------------
This module contains a function that checks if an object is exactly an
instance of a specified class.

Function:
    - is_same_class: Returns True if the object is exactly an instance
      of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is exactly an instance of the specified class,
              otherwise False.
    """
    return type(obj) is a_class
