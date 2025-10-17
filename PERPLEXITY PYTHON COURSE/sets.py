"""
Coding Challenge
Create a set of 5 numbers.

Add a new number to the set.

Remove one number using discard().

Create another set of numbers and perform:

Union

Intersection

Difference

Print all results.
"""

num_set = {1,2,3,4,5}

num_set.add(10)
num_set.discard(1)

num_set2 = {6,7,8,9,10}

print (num_set | num_set2)
print(num_set & num_set2)
print(num_set - num_set2)