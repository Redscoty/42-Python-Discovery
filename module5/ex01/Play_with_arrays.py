#! /usr/bin/env python3
#Ensure this program is executable.
#• Define an array of numbers.
#• Iterate over this array, creating a new array by adding 2 to each value in the original
#array.
#• Your program should contain two arrays: the original array and the modified array.
#• Display both arrays on the screen.

import numpy as np
numbers_array1 = np.array([2, 8, 9, 48, -12, 2])

print(numbers_array1)
print(numbers_array1 + 2)

