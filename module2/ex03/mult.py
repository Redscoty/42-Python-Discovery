#!/usr/bin/python3
number1 = int(input("enter the first number:"))
number2 = int(input("enter a second number:"))
mult_sum = number1 * number2



#f string is telling python to print the variables as text 

result= f"{number1} x {number2} = {mult_sum}"


print(result)

if mult_sum >0:
	print("The result is positive")
elif mult_sum <0:
	print("The result is negative")
else:
	print("The result is zero")

