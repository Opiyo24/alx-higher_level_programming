#!/usr/bin/python3
"""Module the returns a python
data structure froma json string"""

import json


def from_json_string(my_str):
    """treturns pythin representation"""
    return json.loads(my_str)
