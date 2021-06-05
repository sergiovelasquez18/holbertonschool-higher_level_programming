#!/usr/bin/python3
"""
contains the class student
"""


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Inizialites the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary"""
        if attrs is None:
            return self.__dict__
        dict_new = {}
        for s in attrs:
            try:
                dict_new[s] = self.__dict__[s]
            except:
                pass
        return dict_new
