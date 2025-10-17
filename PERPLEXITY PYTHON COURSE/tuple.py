"""
Coding Challenge
Create a tuple of 4 integers.

Print the first and last elements.

Try to change the second element (observe the error).

Count how many times one number appears.

Find the index of a number in the tuple
"""

num_tuple = (1,2,3,4)

print(num_tuple[0])
print(num_tuple[-1])

num_tuple[1] = 4

print(num_tuple.count(3))
print(num_tuple.index(2))