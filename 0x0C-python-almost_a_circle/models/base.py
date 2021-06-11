#!/usr/bin/python3
"""This module creates the Base class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
