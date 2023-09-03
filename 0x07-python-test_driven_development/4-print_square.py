#!/usr/bin/python3

"""Prints a square"""

def print_square(size):

    """print_square - prints a square shape to standard
    output
    Args: size (int): length iof the square"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if (isinstance(size,float) and (size < 0)):
        raise TypeError('size must be an integer')
    length= int(size)
    for i in range(length):
        for j in range(length):
            print('#', end= "")
        print("")