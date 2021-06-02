#!/usr/bin/python3
"""This module defines the append_write function"""


def write_file(filename="", text=""):
    """Read a text file and print it a stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
