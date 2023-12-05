#!/usr/bin/python3
"""Defines the Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student.

        Args:
            first_name (str): student first name.
            last_name (str): student last name.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.Otherwise, all attributes must be retrieved.
        """
        if list == type(attrs) and all(type(ele) == str for ele in attrs):
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
