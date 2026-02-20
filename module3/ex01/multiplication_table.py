#Accepts user input, which will be stored in a numeric variable.
#Display the multiplication table for that number (e.g., if the input is 2, display
#the multiplication table for 2).

#! /usr/bin/env python3

tableNum = int(input("Enter a number to generate its multiplication table: "))
tableSize = range(1,10)
for x in tableSize:
    result = tableNum * x
    print(tableNum," * ",x," = ",result)
