"""
The Problem: Recursive List Summation
Write a function called recursive_sum that calculates the sum of all numbers in a list.
"""

def recursive_sum(data_list):
    if len(data_list) == 0:
        return 0
    else:
        return data_list[0] + recursive_sum(data_list[1:])
numbers = [1,2,3,4]
result = recursive_sum(numbers)
print(f"The recursive sum is: {result}")
