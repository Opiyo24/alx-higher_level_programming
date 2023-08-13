#!/usr/bin/python3

def max_integer(my_list = []):
    if len(my_list) < 1:
        return None
    else:
        placeholder = 0

        for i in range(len(my_list) - 1):
            if my_list[i] > placeholder:
                placeholder = my_list[i]
        return placeholder