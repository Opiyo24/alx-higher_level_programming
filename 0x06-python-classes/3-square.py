#!/usr/bin/python3

"""Class square."""
class Square:
    """Initializing the class."""

    def __init__(self, size = 0);
    """ An instance of the class.

    Args:
        size (int): class size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    self.__size = size

    def area(self):
        """Return the area of square."""

        return (self.__size * self.__size)
