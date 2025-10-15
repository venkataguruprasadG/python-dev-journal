"""
Coding Exercise
Write a script that:

Creates a tuple with three values.

Prints each value using unpacking into separate variables.

Tries to change one value in the tuple (observe what happens).

Prints the error message you receive.
"""

my_tuple =(1, 2, 3) # Creates a tuple with three values
a, b, c = my_tuple  # Unpacks the tuple into separate variables
a = 10 # Tries to change one value in the tuple
print(my_tuple) # Prints the error message you receive