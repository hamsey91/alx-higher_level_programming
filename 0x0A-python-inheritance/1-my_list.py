#!/usr/bin/python3
"""Module for class MyList."""


class MyList(list):
    """Class MyList that inherits from list."""

    def print_sorted(self):
        """Function that print sorted list."""
        print(sorted(self))
