#!/usr/bin/python3
"""
Module: student

This module defines a Student class with public instance attributes
and a method to retrieve its dictionary representation for JSON serialization.

Class:
- Student: Defines a student with first name, last name, and age.
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved. Otherwise, all attributes must be retrieved.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        return self.__dict__
