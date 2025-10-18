"""
Coding Challenge
Create a NumPy array: [1][2][3][4][5][6][7][8][9].

Slice and print the middle three elements.

Reshape the array to shape (3, 3), and print it.

Print the sum of each row.
"""
import numpy as np
numpy_arr = np.array([1,2,3,4,5,6,7,8,9])

numpy_3 = numpy_arr[3:6]
print(numpy_3)

reshaped = numpy_arr.reshape((9,8))
print(reshaped)

print(reshaped.sum(axis=1))