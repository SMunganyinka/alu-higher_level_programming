#!/usr/bin/python3
"""
This module defines a class called Square, which represents a square.

The Square class has a private instance attribute `__size`, which defines
the size of the square. This size is provided during instantiation and
is stored as a private attribute.

The class does not perform any type or value verification for the `size`
attribute.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a new square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private instance attribute
