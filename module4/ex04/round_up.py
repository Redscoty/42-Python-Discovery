#! /usr/bin/env python3

#This program should:
# Prompt the user to enter a number.
# Display the number rounded up.
from math import copysign
user_input =float((input("Enter a number including decimal places: ")))

def _round(x):
    return int(x + 0.5 * copysign(1, x))

print(_round(user_input))