#!/usr/bin/python3
"""Module for is_kind_of_class.."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Returns:
        True if an object is a subclass of a class.
        False if not.
    """
    if isinstance(obj, a_class):
        return True
    return False
