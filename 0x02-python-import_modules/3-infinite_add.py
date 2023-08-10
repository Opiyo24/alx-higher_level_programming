#!/usr/bin/python3
import sys
"""Program that prints the reesult of
teh addition of all arguments

Assume that all argumenst can be cast
into integers

All arguments cast into integers
"""
args = sys.argv
length = len(args)
total = 0

for i in range(1, length):
    total += int(args[i])

print(total)
