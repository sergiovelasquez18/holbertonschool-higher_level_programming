#!/usr/bin/python3
"""This module defines the to _json_string function"""


import json


def from_json_string(my_str):
    """Return the JSON representation of an object (string)"""
    return json.loads(my_str)
