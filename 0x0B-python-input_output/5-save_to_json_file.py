#!/usr/bin/python3
"""This module defines the to _json_string function"""


import json


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of an object (string)"""
    with open(filename, "w", encoding="utf-8") as f:
    	return json.dump(my_obj, f)

