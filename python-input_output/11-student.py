#!/usr/bin/python3
"""
10-student.py
Defines a `Student` class with first name, last name, and age. Includes methods
to serialize (`to_json`) and deserialize (`reload_from_json`) the student instance.
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
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student based on the provided dictionary.

        Args:
            json (dict): A dictionary with the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
