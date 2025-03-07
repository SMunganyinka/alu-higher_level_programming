#!/usr/bin/python3
"""
Function: is_same_class
------------------------
Checks if the object is exactly an instance of the specified class.

Arguments:
    obj: The object to check.
    a_class: The class to compare the object against.

Returns:
    bool: True if the object is exactly an instance of the specified class,
          otherwise False.
"""


def is_same_class(obj, a_class):
    return type(obj) is a_class

