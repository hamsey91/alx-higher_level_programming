#!/usr/bin/python3
"""Defines module for say_my_name."""


def say_my_name(first_name, last_name=""):
    """Function to prints first and last name.

    Args:
        first_name: first name string.
        last_name: last name string.

    Raises:
        TypeError: first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
