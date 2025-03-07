#!/usr/bin/python3
"""
Module: is_kind_of_class
-------------------------
This module contains a function that checks if an object is an instance of, or
if the object is an instance of a class that inherited from, the specified class.

Function:
    - is_kind_of_class: Returns True if the object is an instance of, or an instance
      of a class that inherited from, the specified class, otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is an instance of the specified class,
              or if it is an instance of a subclass of the specified class,
              otherwise False.
    """
    return isinstance(obj, a_class)
