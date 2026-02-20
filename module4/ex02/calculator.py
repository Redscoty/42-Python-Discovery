#! /usr/bin/env python3

User_input1 = int(input(("Give me the first number please: ")))
User_input2 = int(input(("Give me the second number please: ")))

Addition = User_input1 + User_input2
Subtraction = User_input1 - User_input2
Division = User_input1 // User_input2
Multiplication = User_input1 * User_input2

print("Thank you!")
print(f"{User_input1} + {User_input2} = {Addition}")
print(f"{User_input1} - {User_input2} = {Subtraction}")
print(f"{User_input1} / {User_input2} = {Division}")
print(f"{User_input1} * {User_input2} = {Multiplication}")


