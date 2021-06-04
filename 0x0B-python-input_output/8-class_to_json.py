#!/usr/bin/python3
"""This module create a function that returns the dict for JSON serialization"""


def class_to_json(obj):
    """Returns the dictionary description of object"""
    return obj.__dict__
