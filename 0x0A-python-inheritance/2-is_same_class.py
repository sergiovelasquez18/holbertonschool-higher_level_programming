#!/usr/bin/python3
"""This module define the is_same_class funtion"""


def is_same_class(obj, a_class):
    """returns True or False based on inheritance"""
    if type(obj) == a_class:
        return True
    else:
        return False

