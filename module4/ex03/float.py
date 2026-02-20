#! /usr/bin/env python3
#• Create a program called float.py.
#• Ensure this program is executable.
#• This program should:
#◦ Prompt the user to enter a number.
#◦ Determine if the entered number is a decimal or not and display the result.
# a number with decimal is a float
# a number with no decimal is an integer

user_input = input("Enter a number: ")

try:
    number = float(user_input)
    
    if number.is_integer():
        print("This number is an integer")
    else:
        print("this number is a decimal")

except ValueError:
        print("This number is a word, dummy!")

  




