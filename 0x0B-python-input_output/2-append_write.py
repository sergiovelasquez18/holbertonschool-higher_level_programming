#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """Read a text file and print it a stdout"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
