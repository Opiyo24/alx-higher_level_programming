#!/usr/bin/python3

"""Define a class square."""
class Square:
    """Represent the class."""
    def __init__(self, size=0, position=(0, 0)):
        """Initiate the square instance
        
        Args:
            size (int): size of teh square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Get the current position of teh square"""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """The area of the squatre"""
        return (self.__size * self.__size)
    
    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")