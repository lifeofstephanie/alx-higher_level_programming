#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    num = number % 10
else:
    number = -1*number
    num = number % 10
    num = -1*num
    number = -1*number

if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0:
    print(f"Last digit of {number} is {num} and is zero")
else:
    print(f"Last digit of {number} is {num} and is less than 6 but greater than 0")
