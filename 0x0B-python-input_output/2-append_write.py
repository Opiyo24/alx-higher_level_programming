#/usr/bin/python3
"""Module that appends text to a file"""
def append_write(filename="", text=""):
    """Function to append"""
    with open(filename, "a", encoding="UTF-8") as g:
        return(g.write(text))
