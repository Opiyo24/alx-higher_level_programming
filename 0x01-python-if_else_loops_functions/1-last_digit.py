#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = str(number)
length = (len(str_num) - 1)
cmpr = int(str_num[length])
if cmpr > 5:
    print(f"Last digit of {number:d} is {cmpr:d} and is greater than 5")
elif cmpr == 0:
    print(f"Last digit of {number:d} is {cmpr:d} and is 0")
elif cmpr < 0:
    cmpr = (-cmpr)
    print(f"Last digit of {number:d} is {cmpr:d} and is less than 6 and not 0")
elif cmpr < 6 and cmpr != 0:
    print(f"Last digit of {number:d} is {cmpr:d} and is less than 6 and not 0")
