#!/usr/bin/python3
"""square class definition"""


class Square:
    """Represents a square

    Atributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square

        Args:
            size (int): size of a side the square

        Returns: None
        """
        self.__size = size
