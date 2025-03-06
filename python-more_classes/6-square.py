"""
This module defines a Rectangle class to represent a rectangle with the
following functionalities:

1. Private instance attributes `width` and `height` with proper validation.
2. Public class attribute `number_of_instances` that tracks the number of
   `Rectangle` instances.
3. Public class attribute `print_symbol` which allows customization of the
   symbol used for printing the rectangle.
4. Instance methods:
    - `area`: Returns the area of the rectangle.
    - `perimeter`: Returns the perimeter of the rectangle.
    - `__str__`: Returns a string representation of the rectangle.
    - `__repr__`: Returns a string for recreating the rectangle instance.
5. Destructor (`__del__`) that decrements `number_of_instances` and prints a
   farewell message upon deletion.

The class enforces the following rules:
- The `width` and `height` attributes must be integers and must be ≥ 0.
- If either `width` or `height` is 0, the perimeter is 0, and the string
  representation is an empty string.

Example usage:
    rect = Rectangle(4, 3)
    print(rect.area())        # 12
    print(rect.perimeter())   # 14
    print(str(rect))          # Prints rectangle with '#' symbols
    del rect                  # Prints "Bye rectangle..."
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (any): Symbol used to represent the rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The width to be set for the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The height to be set for the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The rectangle represented by the character(s) in print_symbol.
            An empty string if the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """
        Return a string that can be used to recreate the rectangle.

        Returns:
            str: The string representation of the rectangle for eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when an instance is deleted and decrement the instance count.

        Outputs:
            Bye rectangle...
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
