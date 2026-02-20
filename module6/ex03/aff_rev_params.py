#! /usr/bin/env python3


import sys

matches = []  #made a flag

for arg in sys.argv[1:]:
    if not arg.isdigit(): # all inputs are string by default so check whether it is digits
        matches.append(arg)  # when a match is found it appends the match
    
if len(matches) <2: # makes a condition
    print("none")    
else:
    for arg in matches[::-1]:
        print(arg)


