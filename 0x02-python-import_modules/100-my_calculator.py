#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
"""Imports all fuctions from calculator_1.py
and handles basic oprations
"""
"""Check number of arguments"""
argument = sys.argv
length = len(argument)
"""If number of arguments is not three"""
if length != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
else:
    argument[1] = int(argument[1])
    argument[3] = int(argument[3])
    ans = 0
    """addition"""
    if argument[2] == "+":
        operator = "+"
        ans = add(argument[1], argument[3])
    elif argument[2] == "-":
        operator = "-"
        ans = sub(argument[1], argument[3])
    elif argument[2] == "*":
        operator = "*"
        ans = mul(argument[1], argument[3])
    elif argument[2] == "/":
        operator = "/"
        ans = div(argument[1], argument[3])
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

print(f"{argument[1]} {operator} {argument[3]} = {ans}")
"""If operator is...elif...else print unknown"""