#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """Defines a rectangle with width and height attributes."""

    number_of_instances = 0  # Class attribute to track the number of instances
    print_symbol = "#"  # Class attribute for the symbol used in string representation

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                         for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation to recreate a new instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance is deleted."""
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
        print("Bye rectangle...")
