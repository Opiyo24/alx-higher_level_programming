#!/usr/bin/python3

if __name__ == "__main__":
    """Print trhe sum, difference, multiple and quotient of 10 and 5"""
    from calculator_1 import add, sub, mul, div

    """My operation functions
    """
    a = 10
    b = 5
    """addition"""
    addition = add(a, b)
    print(f"{a:d} + {b:d} = {addition:d}")

    """Subtraction"""
    subtraction = sub(a, b)
    print(f"{a:d} - {b:d} = {subtraction:d}")

    """Multiplication"""
    multiplication = mul(a, b)
    print(f"{a:d} * {b:d} = {multiplication:d}")

    """Division"""
    division = div(a, b)
    print(f"{a:d} / {b:d} = {division:0.0f}")
    """Cast division to 0 decimal float
    python defaults divisions to float type"""
