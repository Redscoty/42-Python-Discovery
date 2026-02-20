#Create a program called advanced_mult.py.
#Ensure the program is executable.
#The program should:
#Display all multiplication tables from 0 to 10 in the following format:
#start the program with a variable that represents the table number
#start at 0
#set a condition for the loop to stop at 10
#! /usr/bin/env python3

tableNum = 0  #starting number we want to multiply

while tableNum < 10:  # limit the range to a max of 10
    print (f"table of {tableNum}: ", end="") #1st loop prints "table of 1 upto 10"

    col_number = 0
    while col_number <= 10:
        print(tableNum * col_number, end=" ")  
        col_number += 1   # counter for the col num
    
    print()
    tableNum += 1  # counter for the table num