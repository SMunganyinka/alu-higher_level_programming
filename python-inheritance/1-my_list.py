#!/usr/bin/python3
"""
This module defines a custom class `MyList` that inherits from the built-in 
`list` class. It adds a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of `list` that includes a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list but prints a sorted 
        version of it.
        """
        print(sorted(self))

