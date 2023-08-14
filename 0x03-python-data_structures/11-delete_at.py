#!/usr/bin/python3

def delete_at(my_list = [], idx = 0):
    """Deletes a list element at a certain index
    
    Args:
        my_list: The list
        idx: specified index
        
    Returns:
        New list
    """
    if idx >= 0 and idx <= len(my_list):
        del my_list[idx]
    return my_list