"""
The Challenge: Data Cleanup
You have a list of raw data entries that needs processing:

Python

raw_data = [10, 5, 20, 15, 5, 30]

Your tasks are:

Sorting: Write one line to sort the raw_data list in place (modify the original list) 
from smallest to largest.

Counting: Write one line to count how many times the number 5 appears in the list and print the result.

Slicing (The DSA Concept): Create a new list named top_three by extracting
the three largest numbers from the sorted raw_data list using slicing syntax ([:]).
"""

raw_data = [10,5,20,15,5,30]

print(raw_data.sort())

print(raw_data.count(5))

top_three = raw_data[-3:]

print(top_three)