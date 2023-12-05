#!/usr/bin/python3
"""Defines function that read a text file."""


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdou."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
