#!/usr/bin/python3
"""Defines a square class module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor.

        Args:
            size (int): The square size.
            x (int): the horizontal axis x of square.
            y (int): the vertical axis y of square.
            id (int): the identity of the square.
        """
        super().__init__(size, size, x, y, id)
