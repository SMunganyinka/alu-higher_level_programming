#!/usr/bin/python3
"""
9-student.py
Defines a `Student` class with first name, last name, and age.
Includes a method `to_json` that returns a dictionary representation of the
student. The dictionary can contain all attributes or a subset specified
by the user.
"""

class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with the provided attributes.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student.

        If `attrs` is provided, only the specified attributes are included.

        Args:
            attrs (list, optional): List of attribute names. Defaults to None.

        Returns:
            dict: Dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__
