"""
Coding Exercise
Write a function sum_all(*numbers) that:

Accepts any number of positional numeric arguments.

Returns their sum.

Test it with different counts of arguments.
"""

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_all(1,2,3,4,5)) # 15
print(sum_all(10,20))     # 30

print("Another Method ")

def sum_all_numbers(*num):
    return sum(num)
print(sum_all_numbers(1,2,3)) # 6