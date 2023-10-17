#!/usr/bin/python3
"""Module for class rectangle"""
class Rectangle:
    """Initializing class rectangle"""
    def __init__(self, width=0, height=0):
        """Instance of class rectangle
        Args:
            height (optional): height
            width (optional): width
        """
        self.height = height
        self.width = width
    
    @property
    def width(self):
        """Property get - width
        Return:
            width
        """
        return (self.__width)
    @width.setter
    def width(self, value):
        """Set width value
        Args:
            value (int): new width value
        Raises:
            TypeError if width is not int
            ValueError if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    
    @property
    def height(self):
        """Property setter - height
        Return:
            height
        """
        return (self.__height)
    
    @height.setter
    def height(self, value):
        """Set width value
        Args:
            value (int): new height value
        Raises:
            TypeError if height is not int
            ValueError if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    
    def area(self):
        """Calculates rectangle area
        Return:
            Area
        """
        return (self.__height * self.__width)
    
    def perimeter(self):
        """Calculates rectangle perimeter
        Return:
            Perimeter
        """
        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        return (2 * (self.__height + self.__width))
    
    def __str__(self):
        """Comments"""
        if self.__width ==0 or self.__height == 0:
            return("")
        
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))