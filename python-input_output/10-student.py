#!/usr/bin/python3
"""
9-student.py
This module defines a `Student` class that represents a student with first name,
last name, and age. It includes a method `to_json` to return a dictionary representation
of a Student instance. The dictionary can contain all attributes or a subset of attributes
specified by the user.

Attributes:
    first_name (str): The student's first name.
    last_name (str): The student's last name.
    age (int): The student's age.

Methods:
    to_json(attrs=None): Retrieves a dictionary representation of the Student instance.
                          If `attrs` is provided, only the specified attributes are included.
"""


class Student:
    """A class that defines a student by their first name, last name, and age."""

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

        If the attrs argument is provided as a list of strings, only the attributes
        in that list will be included in the returned dictionary. If attrs is None
        or invalid, all attributes of the student instance will be returned.

        Args:
            attrs (list, optional): A list of attribute names to retrieve. 
                                    Defaults to None.

        Returns:
            dict: A dictionary representation of the student, containing the specified
                  attributes or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
