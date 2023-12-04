#!/usr/bin/python3
"""Module for class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rectangle."""
    def __init__(self, width, height):
        """Intialize Rectangle.

        Args:
            width: The width of Rectangle.
            height: The height of Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
