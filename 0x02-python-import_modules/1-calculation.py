#!/usr/bin/python3

if __name__ == "__main__":
    """Print trhe sum, difference, multiple and quotient of 10 and 5"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    addition = add(a, b)
    print(f"{a:d} + {b:d} = {addition:d}")
    subtraction = sub(a, b)
    print(f"{a:d} - {b:d} = {subtraction:d}")
    multiplication = mul(a, b)
    print(f"{a:d} * {b:d} = {multiplication:d}")
    division = div(a, b)
    print(f"{a:d} / {b:d} = {division:0.0f}")
