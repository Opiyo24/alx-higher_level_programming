#!/usr/bin/python3
"""Prints text with newlines."""

def text_indentation(text):

    """
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    
    result = []

    for i in range(len(text)):
        result.append(text[i])
        if text[i] in ".?:":
            result.append('\n\n')
    
    string = ''.join(result)
    print(string, end = "")