#!/usr/bin/python3
"""Module for inherits_from."""


def inherits_from(obj, a_class):
    """Function that check if the object is an instance
       of a class that inherited.

    Returns:
        True.
        False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
