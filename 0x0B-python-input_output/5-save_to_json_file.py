#!/usr/bin/python3
"""Module that saves python onject"""
import json

def save_to_json_file(my_obj, filename):
    """Saves an object to json file"""
    with open(filename, "w") as h:
        json.dump(my_obj, h)
