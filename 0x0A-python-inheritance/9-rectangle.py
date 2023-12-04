#!/usr/bin/python3
"""Module for class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rectangle."""

    def __init__(self, width, height):
        """Intialize Rectangle.

        Args:
            width: The width of Rectangle.
            height : The height of Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to calculate the area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Method representation of a Rectangle as string."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
