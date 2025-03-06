#!/usr/bin/python3
"""
This module defines a Rectangle class to represent a rectangle.

Features:
- Private attributes `width` and `height` with validation.
- Class attributes:
  - `number_of_instances`: Tracks the number of instances.
  - `print_symbol`: Used to print the rectangle.
- Methods:
  - `area()`: Returns the area.
  - `perimeter()`: Returns the perimeter.
  - `__str__()`: Returns a string representation.
  - `__repr__()`: Returns a recreation string.
  - `__del__()`: Prints a message when deleted.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        number_of_instances (int): Tracks the number of instances.
        print_symbol (any): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.

        Args:
            width (int): The rectangle width (default 0).
            height (int): The rectangle height (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width.

        Args:
            value (int): The width.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height.

        Args:
            value (int): The height.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter.

        If width or height is 0, return 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Uses `print_symbol` for display.
        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width]
            * self.__height
        )

    def __repr__(self):
        """
        Return a string that recreates the instance.
        """
        return (
            f"Rectangle({self.__width}, {self.__height})"
        )

    def __del__(self):
        """
        Print message and decrement instance count when deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
