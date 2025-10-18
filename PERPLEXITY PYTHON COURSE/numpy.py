"""
Coding Challenge
Import NumPy and create a 1D array containing numbers 10, 20, 30, 40, 50.

Print the type, shape, and size of your array.

Create a 2D array [[1][2][3], [4][5][6]] and print it
"""

import numpy as np          # Standard convention

arr = np.array([10, 20, 30, 40, 50])
print(arr.dtype)            # e.g. int64
print(arr.shape)            # (5,)
print(arr.size)             # 5

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)               # Prints a proper 2D array grid
