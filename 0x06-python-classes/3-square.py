#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines square."""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size (int): The side length of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area."""
        return (self.__size * self.__size)
