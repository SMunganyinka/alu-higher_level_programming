#!/usr/bin/python3
"""
Module: base_geometry
---------------------
This module defines the `BaseGeometry` class.

Classes:
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

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Args:
            name (str): The name of the parameter (assumed to be a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
