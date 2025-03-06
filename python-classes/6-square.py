#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

The class has the following methods:
- __init__(size=0, position=(0, 0)): Initializes a square with a given size
  and position.
- size: Property to get the size of the square.
- size.setter: Setter to set the size, with validation for integer type and
  non-negative values.
- position: Property to get the position of the square.
- position.setter: Setter to set the position, with validation for a tuple
  of two positive integers.
- area(): Method to calculate and return the area of the square.
- my_print(): Method to print the square using the '#' character, with
  the specified position.

The square's size and position can be optionally set during initialization.
If no size or position is provided, the default values are 0 and (0, 0).
"""

class Square:
    """
    A class that defines a square by its size and position.

    Attributes:
        __size (int): The size of the square (private attribute).
        __position (tuple): The position of the square (private attribute).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with a given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of
                        two positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two positive integers representing the
                           new position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        The position will adjust the printed square accordingly.
        """
        if self.__size == 0:
            print()
        else:
            # Print leading empty lines based on position[1]
            for i in range(self.__position[1]):
                print()
            # Print the square itself, with leading spaces based on position[0]
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
