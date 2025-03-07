#!/usr/bin/python3
"""
Rectangle module.

This module defines a Rectangle class which inherits from the BaseGeometry class. 
It ensures that both the width and height of the rectangle are positive integers 
and validates them using the integer_validator method from the BaseGeometry class.
"""

class Rectangle(BaseGeometry):
    """A class representing a rectangle that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        
        self.__width = width  # Private attribute for width
        self.__height = height  # Private attribute for height
