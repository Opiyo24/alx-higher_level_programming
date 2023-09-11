#!/bin/usr/python3
"""Class module that raises an exception"""
class BaseGeometry:
    """base class"""
    def area(self):
        """class attribute"""
        raise Exception("area() is not implemented")
