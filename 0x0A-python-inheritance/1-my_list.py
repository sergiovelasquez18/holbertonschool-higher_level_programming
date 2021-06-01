#!/usr/bin/python3
"A module that difines a class named Mylist"


class MyList(list):
    """A classe the Mylist"""

    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints instace"""
        print(sorted(self))
