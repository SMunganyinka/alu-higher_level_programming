#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

The class has the following methods:
- __init__(size=0): Initializes a square with the given size.
- size: Property to get the size of the square.
- size.setter: Setter to set the size, with validation for integer type and
  non-negative values.
- area(): Method to calculate and return the area of the square.
- my_print(): Method to print the square using the '#' character.

The square's size can be optionally set during initialization. If no size
is provided, the default value is 0.
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

    def my_print(self):
        """
        Prints the square in stdout using the '#' character.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
