#!/usr/bin/python3
"""
Rectangle module.

This module defines the Rectangle class that inherits from BaseGeometry.
It ensures that both the width and height are positive integers and validates
them using the integer_validator method from the BaseGeometry class.
"""

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Validates:
            width and height must be positive integers.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width  # Private attribute for width
        self.__height = height  # Private attribute for height
