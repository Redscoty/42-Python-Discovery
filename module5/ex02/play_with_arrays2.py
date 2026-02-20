import numpy as np
numbers_array1 = np.array([2, 8, 9, 48, 8, 22, -12, 2])

a = numbers_array1 + 2



#created a condition, retrns true of false for each value relative to >5
b = a > 5 
#print(b)

#extracts each value that was true relative to the set condition
numbers_array2 = np.extract (b, a)

print(np.array2string(numbers_array1, separator=","))
print(np.array2string(numbers_array2, separator=", "))


