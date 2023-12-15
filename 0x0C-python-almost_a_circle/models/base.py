#!/usr/bin/python3
"""Defines a base classe module."""
from json import dumps, loads
import csv


class Base:
    """Representation of the "base" of all classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base.

        Args:
            id (int): The identity of the base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
