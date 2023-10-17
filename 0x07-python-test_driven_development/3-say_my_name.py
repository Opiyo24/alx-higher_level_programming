#!/usr/bin/python3
"""Prints My name is <first_name> <last_name>"""
def say_my_name(first_name, last_name=""):
    """say_my_name - prints the first name then last name.
    Args:
        first_name (str): first arg.
        last_name (str): second arg."""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))