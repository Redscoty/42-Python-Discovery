#! /usr/bin/env python3
#sys.argv will return any arguments in thecommand line when the script is Run
#I only want the first string. 
#I need to define the arg as a string and then tell it that
#argument is anything else it should print none.

import sys

matches = []  #made a flag

for arg in sys.argv[1:]:
    if not arg.isdigit(): # all inputs are string by default so check whether it is digits
        matches.append(arg)  # when a match is found it appends the match
    
if len(matches) == 1: # makes a condition so it can only print match 1
    print(matches[0].lower())    
else:
    print("None")
