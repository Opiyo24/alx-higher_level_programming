#!/usr/bin/python3
"""Module that prints a sorted list"""

class MyList(list):
    """Child class of object list"""
    
    def print_sorted(self):
        """Function that sorts a list"""
        print(sorted(self))
