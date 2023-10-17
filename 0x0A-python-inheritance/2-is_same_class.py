#!/usr/bin/python3
"""Module that examines the instance of an object"""
def is_same_class(obj, a_class):
    """is_same_class - checks if an object isd an instance of a class
    Args:
        obj: object to examine
        a_class: the class in question
    Return: True is object is instance of c,as
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
