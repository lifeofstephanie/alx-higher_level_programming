#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    num = number % 10
else:
    number = -1*number
    num = number % 10

if num > 5:
    print(f"The last digit of {number} is {num} and it's greater than 5")
elif num == 0:
    print("0")
else:
    print(f"The last digit of {number} is {num} and it is less than 6 but greater than 0")
