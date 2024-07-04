#!/usr/bin/python3
"""Module to find a Peak  for list of integers."""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
