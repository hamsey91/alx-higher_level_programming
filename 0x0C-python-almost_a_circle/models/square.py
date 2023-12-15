#!/usr/bin/python3
"""Defines a square class module."""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor.

        Args:
            size (int): The square size.
            x (int): the horizontal axis x of square.
            y (int): the vertical axis y of square.
            id (int): the identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the square size."""
        self.width = value
        self.height = value

    def f_update(self, id=None, size=None, x=None, y=None):
        """Method that assigns an argument to each attribute."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args.

        Args:
            *args (ints): The attribute values:
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): The double pointer to a dictionary key/value.
        """
        if args:
            self.f_update(*args)
        elif kwargs:
            self.f_update(**kwargs)

    def to_dictionary(self):
        """Method for the dictionary representation of a square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns rectangle information in string type."""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
