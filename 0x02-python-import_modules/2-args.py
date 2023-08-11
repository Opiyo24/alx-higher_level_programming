#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    """My function prints the number of arguments
    passed to it in the command line
    """
    args = sys.argv
    #print(args)
    length = len(args)

    if length == 0:
        print("0 arguments")
    elif length == 1:
        print("1 argument")
        print(f"{length:d}: {args[0]}")
    else:
        print(f"{length:d} arguments")
        for i in range(length):
            print(f"{(i + 1):d}: {args[i]}")
