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
