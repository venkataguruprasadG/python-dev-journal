"""
Coding Challenge 1: Data Filtering and Transformation
Problem:

Given the following list of user session lengths (in seconds):

Python

session_seconds = [1800, 7200, 300, 4500, 5000, 3500, 10800]
Write a single line of Python code using a list comprehension to create a new list that contains:

Only sessions that are longer than 3600 seconds.

The session length converted from seconds to hours (i.e., divided by 3600).

The result should be rounded to 2 decimal places.
"""

session_seconds = [1800, 7200, 300, 4500, 5000, 3500, 10800]

longest_hours = [round(i/3600,2) for i in session_seconds if i > 3600]

print(longest_hours)