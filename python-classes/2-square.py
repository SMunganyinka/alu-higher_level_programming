#!/usr/bin/python3
"""
This module defines a class called Square, which represents a square.

The Square class has a private instance attribute `__size`, which defines
the size of the square. This size is provided during instantiation and is
stored as a private attribute.

The class performs validation to ensure the size is an integer and that
it is greater than or equal to 0. If the validation fails, it raises
appropriate exceptions (TypeError or ValueError).
"""

class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """
        Initializes a new square with a given size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private instance attribute
