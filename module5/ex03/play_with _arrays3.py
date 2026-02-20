#! /usr/bin/env python3

import numpy as np
numbers_array1 = np.array([2, 8, 9, 48, 8, 22, -12, 2])

a = numbers_array1 + 2

#created a condition, retrns true of false for each value relative to >5
b = a > 5 
#print(b)

#extracts each value that was true relative to the set condition
numbers_array2 = np.extract (b, a)

#numbers_array3 = np.unique(numbers_array2)
numbers_array3 = set(numbers_array2)
numbers_array3 = np.array(list(numbers_array3))
print(numbers_array3)

print("original array:")
print(np.array2string(numbers_array1, separator=","))

print("OG array + 2")
print(a)

print("OG array +2 >5")
print(np.array2string(numbers_array2, separator=", "))

print("unique array:") # my output is technically wrong because I have not output the data as a set. I need to ensure the data is handled as a set.
x = set(np.array2string(np.sort(numbers_array3), separator=", "))
#print((np.array2string(np.sort(numbers_array3), separator=", ")))
print(x)
