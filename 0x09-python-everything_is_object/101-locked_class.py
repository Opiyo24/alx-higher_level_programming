#!/usr/bin/python3
"""Locked class"""

class LockedClass:
    """
    Cannot instantiate unless
    attribute is 'first_name'
    """
    __slots__ = ["first_name"]
