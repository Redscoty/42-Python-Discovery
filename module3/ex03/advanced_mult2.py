
#! /usr/bin/env python3
tableNum = 0

while tableNum < 10:
    print (f"table of {tableNum}: ", end=" ")

    col_number = 0
    while col_number <= 10:
        print(tableNum * col_number, end=" ")
        col_number += 1
    print()
    tableNum += 1
