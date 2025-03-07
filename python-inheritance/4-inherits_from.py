#!/usr/bin/python3
"""
Module: inherits_from
----------------------
This module contains a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from the specified class.

Function:
    - inherits_from: Returns True if the object is an instance of a class that
      inherited from the specified class, otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is an instance of a subclass of the specified
              class (but not an instance of the specified class itself),
              otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
