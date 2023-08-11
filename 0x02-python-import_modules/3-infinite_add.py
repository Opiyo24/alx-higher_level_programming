#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    import sys

    args = sys.argv
    length = len(args)
    total = 0

    for i in range(1, length):
        total += int(args[i])

    print(total)
