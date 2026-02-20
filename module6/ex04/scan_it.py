#! /usr/bin/env python3


import sys
import re

match = []  #made a flag
    
if len(sys.argv) !=3: # makes a condition
    print("none")    
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    matches = re.findall(keyword, text)
    print(len(matches))
