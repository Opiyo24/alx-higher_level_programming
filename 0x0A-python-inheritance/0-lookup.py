#!/usr/bin/python3
"""module with function that prints the attributes
    and methods of an object
"""
def lookup(obj):
    """Function that returns the available attributes and
    methods of an object
    """
    return(dir(obj))
