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

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Returns rectangle information in string type."""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def first_update(self, id=None, width=None, height=None, x=None, y=None):
        """Method that assigns an argument to each attribute."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args.
	Args:
            *args (ints): The attribute values:
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): The double pointer to a dictionary key/value.
        """
        if args:
            self.first_update(*args)
        elif kwargs:
            self.first_update(**kwargs)
