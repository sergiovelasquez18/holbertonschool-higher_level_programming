#!/usr/bin/python3
"""This module creates the Base class"""


class Base:
    """Class name base
    Attributes:
    atrr1(__nb_object): numbert the objects
    attr2(id): object id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
