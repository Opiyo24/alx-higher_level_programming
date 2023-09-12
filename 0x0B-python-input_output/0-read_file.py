#!/usr/bin/python3
"""Module opens and reads a text file UTF-8"""
def read_file(filename=""):
    """Function to read the contents of a file"""
    with open(filename, "r", encoding='UTF-8') as file:
        print(file.read())
