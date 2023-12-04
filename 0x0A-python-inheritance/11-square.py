#!/usr/bin/python3
"""Module class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing the square."""

    def __init__(self, size):
        """Initialize the square.

        Args:
            size: The size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method for area of square."""
        return self.__size ** 2

    def __str__(self):
        """String representation of this square."""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
