#!/usr/bin/python3
"""Defines a rectangle class module."""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle.

        Args:
            width (int): the rectangle width.
            height (int): the rectangle height.
            x (int): The horizontal axis x  of rectangle.
            y (int): The vertical axis y of rectangle.
            id (int): The identity of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter/setter for width of this rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """getter/setter for height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """getter/setter for axis x of this rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """getter/setter for axis y of this rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
