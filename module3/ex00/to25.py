#! /usr/bin/env python3
#Accepts user input, which will be stored in a numeric variable.
#◦ Use a loop to display all numbers from en entered number up to 25.
#◦ If the input number is greater than 25, display "Error" followed by a new line


userinput = int(input("Enter a number less than 25:") )

if userinput > 25:
    print("Error")
else:
    for num in range(userinput,25):
        print(f"Inside the loop, my variable is {num}")
              
    

