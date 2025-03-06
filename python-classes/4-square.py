#!/usr/bin/python3
"""
This module defines a class called Square, which represents a square.

The Square class has a private instance attribute `__size`, which defines
the size of the square. This size is provided during instantiation and is
stored as a private attribute.

The class performs validation to ensure the size is an integer and that
it is greater than or equal to 0. If the validation fails, it raises
appropriate exceptions (TypeError or ValueError).

Additionally, the class includes a public method `area()` to calculate
and return the area of the square. It also has a getter and setter for the
private `size` attribute.
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
        self.size = size  # Using the setter to apply validation

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private attribute assignment

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
