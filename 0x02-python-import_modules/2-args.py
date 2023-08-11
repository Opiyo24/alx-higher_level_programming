#!/usr/bin/python3

if __name__ == "__main__":
    """Prints number and list of arguments"""
    import sys

    args = sys.argv
    length = len(args)
    
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print("{}: {}".format(length, args[1]))
    else:
        print("{} arguments".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format((i), args[i]))
