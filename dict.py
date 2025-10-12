"""Coding Exercise
Write a script that:

Creates a dictionary with three key-value pairs.

Adds a new key-value pair.

Updates the value of an existing key.

Removes a key.

Prints all keys and values."""

my_dict = {'a': 1, 'b' : 2,'c' : 3} # Creates a dictionary with three key-value pairs
my_dict['d'] = 4 # Adds a new key-value pair
my_dict['a'] = 10 # Updates the value of an existing key
del my_dict['b'] # Removes a key
print(my_dict) # Prints all keys and values

