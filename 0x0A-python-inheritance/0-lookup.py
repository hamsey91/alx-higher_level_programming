#!/usr/bin/python3
"""Module for Lookup."""


def lookup(obj):
    """Function that returns the list of available attributes.
    Returns:
        A list object.
    """
    return dir(obj)
