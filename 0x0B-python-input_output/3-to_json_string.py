#!/usr/bin/python3
"""Defines function that represents JSON string."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of a object(string)."""
    return json.dumps(my_obj)
