#!/usr/bin/python3
"""Checks id object is an instance of a class"""
def inherits_from(obj, a_class):
    """Checks if object is an instyance of class"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
