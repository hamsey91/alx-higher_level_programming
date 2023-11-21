#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines square."""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size (int): The side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the side length of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area."""
        return (self.__size * self.__size)
