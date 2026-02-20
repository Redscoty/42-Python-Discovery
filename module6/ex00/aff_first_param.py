#! /usr/bin/env python3
#sys.argv will return any arguments in thecommand line when the script is Run
#I only want the first string. 
#I need to define the arg as a string and then tell it that
#argument is anything else it should print none.

import sys

for arg in sys.argv[1:]:
    if not arg.isdigit(): # all inputs are string by default so check whether it is digits
        print(arg)
        break #without a break the program loops and would print all none digit inputs but would also print none

        
else:
    print("None")


#If I wanted the script to print all non digit command line items then it would need a flag.
#If you just remove break, the program will continue looping not knowing if it has found a match.
# A flag is like an on/off switch that would be triggered in case of a match.

#matchfound=false
# in the loop under if would be matchfound=true
# at the end print"none" would be conditional on if not matchfound: print....