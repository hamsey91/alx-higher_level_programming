#!/usr/bin/python3
"""Defines a rectangle class module."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor.

        Args:
            width (int): the rectangle width.
            height (int): the rectangle height.
            x (int): the horizontal axis x of rectangle.
            y (int): the vertical axis y of rectangle.
            id (int): the identity of the rectangle.
        Raises:
            TypeError: If the input (width & height) is not an integer.
            ValueError: If width or height is under or equals 0.
            TypeError: If the input (x & y) is not an integer.
            ValueError: If x or y is under 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter/setter for width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter/Setter for height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter/Setter for the axis x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter/Setter for the axis y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle instance."""
        return self.width * self.height
