#!/usr/bin/python3
"""
Module for writing a string to a UTF-8 encoded text file.

This module provides a function to write a given string into a text file.
If the file does not exist, it will be created. If the file exists, its
contents will be overwritten.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 encoded text file and returns the number
    of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
