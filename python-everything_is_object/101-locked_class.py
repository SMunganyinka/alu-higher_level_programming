#!/usr/bin/python3
"""
This module defines a LockedClass that restricts dynamic attribute creation.

Users can only create an instance attribute called 'first_name'.
Any attempt to create other attributes will raise an AttributeError.
"""


class LockedClass:
    """
    A class that prevents dynamic attributes except 'first_name'.

    Attributes:
        first_name (str): Allowed instance attribute.
    """

    __slots__ = ['first_name']
