#!/usr/bin/python3
"""Module that writes a string toa  text file
and returns the num ber of characters written"""
def write_file(filename="", text=""):

    with open(filename, "w", encoding='UTF-8') as file:
        return file.write(text)
