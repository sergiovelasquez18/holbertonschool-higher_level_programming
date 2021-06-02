#!/usr/bin/python3
"""This module defines the read_file function"""


def write_file(filename="", text=""):
    """Read a text file and print it a stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
