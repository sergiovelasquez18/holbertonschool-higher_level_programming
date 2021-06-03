#!/usr/bin/python3
"""This module defines the read_file function"""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""
    return json.dumps(my_obj)
