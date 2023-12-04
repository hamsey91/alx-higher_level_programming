#!/usr/bin/python3
"""Module for is_same_class."""


def is_same_class(obj, a_class):
    """Function to check if an object is exactly an instance of a class.

    Returns:
        True if the object is exactly an instance of the specified class
        False if not.
    """
    if type(obj) == a_class:
        return True
    return False
