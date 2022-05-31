#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = (-1 * number % 10) * -1
else:
    num = number % 10
if num > 5:
        print(f"Last digit of {number:d} is {num:d} greater than 5")
elif num == 0:
    print(f"Last digit of {number:d} is {num:d} is 0 ")
elif num < 6 and num != 0:
    print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0 ")
