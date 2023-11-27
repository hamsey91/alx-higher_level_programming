#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Representation a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle.

        Args:
            width : The rectangle width.
            height: The rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter & setter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter & setter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return printable representation of the rectangle with
        the # character."""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))

        return string

    def __repr__(self):
        """return the string representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
