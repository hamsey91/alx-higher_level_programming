#!/usr/bin/python3
"""Module class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing the square."""

    def __init__(self, size):
        """Initialize square.

        Args:
            size: The size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
