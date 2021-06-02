#!/usr/bin/python3
"""This module define the is_same_class funtion"""


def inherits_from(obj, a_class):
    """returns True or False based on inheritance"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
