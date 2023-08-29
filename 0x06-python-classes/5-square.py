#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent the square"""

    def __init__(self, size):
        """Initialize the square

        Args:
            size (int): size of the square
        """
        self.size = size

        @property
        def size(self):
            """Get the size value"""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the value of size"""
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Return the area f the square"""
            return (self.__size * self.__size)

        def my_print(self):
            """Print teh square with the # character"""
            for i in range(0, self.__size):
                [print("#", end = "") for j in range(self.__size)]
                print("")
            if self.__size == 0:
                print("")
