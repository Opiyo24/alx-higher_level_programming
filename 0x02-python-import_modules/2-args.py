#!/usr/bin/python3
if __name__ == "__main__":
    """Prints number and list of arguments"""
    import sys

    args = sys.argv
    length = len(args)

    if length == 0:
        print("0 arguments")
    elif length == 1:
        print("1 argument")
        print("{}: {}".format(length, args[0]))
    else:
        print("{} arguments".format(length))
        for i in range(length):
            print("{}: {}".format((i + 1), args[i]))
