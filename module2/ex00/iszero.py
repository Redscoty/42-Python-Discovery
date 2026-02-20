#! /usr/bin/env python3

number = int(input("enter a number:"))
reference_value=0

# this line sets the permissions

#chmod u+x iszero.py this is placed in the terminal cammand line before then running this script. it ensures access. 
# remember to be consistent between integers and strings, did not work initially because you were comparing a string to an integer.


#setting the if functions
if number == reference_value:
	print("This number is equal to zero")
else:
	print("This number is different to zero")
#if number != reference_value:
	#print("This number is different to", reference_value)



