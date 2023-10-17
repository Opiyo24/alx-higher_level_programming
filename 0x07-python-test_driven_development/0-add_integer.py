#!/usr/bin/python3
"""Function that adds two integers or floats
Raises Type error with message in case of type error
Args:
    Takes two arguments, one is defaulted to 98
Returns the ssum of the two numbers."""
def add_integer(a, b=98):
    """add_integer - function that adds two integers
    Args:   a (int/ float): first argument
            b (int/ float): secont parameter"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    return int(a + b)