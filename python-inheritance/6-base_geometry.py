#!/usr/bin/python3
"""
Module: base_geometry
---------------------
This module defines the `BaseGeometry` class.

Class:
    - BaseGeometry: A base class for geometric operations.
"""


class BaseGeometry:
    """
    A base class for geometric operations.
    """

    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")
