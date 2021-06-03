#!/usr/bin/python3
"""This module defines the to _json_string function"""


import json


def load_from_json_file(filename):
    """Return the JSON representation of an object (string)"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
