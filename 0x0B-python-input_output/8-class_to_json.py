#!/usr/bin/python3
"""Defines the function class-to-json."""


def class_to_json(obj):
    """Returns the dictionary description with a simple data structure."""
    return obj.__dict__
