#!/usr/bin/python3
"""Defines the Student class."""


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize Student.

        Args:
            first_name : student first name.
            last_name : student last name.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returs a dictionary representation of the Student instance."""
        return self.__dict__
