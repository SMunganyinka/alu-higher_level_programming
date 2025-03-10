#!/usr/bin/python3
"""
Module for reading and printing the contents of a UTF-8 encoded text file.

This module provides a function to read a text file and print its contents
to the standard output using the `with` statement for proper file handling.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty
        string.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
