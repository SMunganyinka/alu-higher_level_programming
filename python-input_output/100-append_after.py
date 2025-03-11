#!/usr/bin/python3
"""
This module provides a function to insert a line of text
into a file after each line containing a specific string.

Functionality:
- Reads a file line by line.
- Checks if a given search string is present in each line.
- If found, inserts a new line of text immediately after it.
- Writes the updated content back to the file.

Usage:
    append_after("filename.txt", "target_string", "new_line\n")
"""

def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string."""

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
