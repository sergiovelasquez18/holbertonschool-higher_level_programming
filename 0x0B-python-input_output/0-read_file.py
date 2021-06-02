#!/usr/bin/python3
"""This module defines the read_file function"""


def read_file(filename=""):
    """Read a text file and print it a stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
