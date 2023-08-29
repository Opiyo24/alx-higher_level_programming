#!/usr/bin/python3

"""A class square."""
class Square:
    """ Representing a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the new square.
        """
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
