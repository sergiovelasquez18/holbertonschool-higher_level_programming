#!/usr/bin/python3
"""This module creates the Square class thst inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class named Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of the Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return the informal representation of Square class"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
