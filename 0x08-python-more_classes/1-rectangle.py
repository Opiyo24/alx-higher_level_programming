#!/usr/bin/python3
"""Module for Class rectangle"""
class Rectangle:
    """Defining class rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing rectangle
        Args:
            height (optional): height of rectangle
            width (optional): width of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width attribute getter
        Return:
            width of rectangle
        """
        return (self.__width)
    
    @width.setter
    def width(self, value):
        """Attribute setter
        Args:
            value: New attribute value
        Return:
            New width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    
    @property
    def height(self):
        """Height attribute getter
        Return:
            Height of rectangle
        """
        return (self.__height)
    
    @height.setter
    def height(self, value):
        """Attribute setter
        Args:
            value: New attribute value
        Return:
            New height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value