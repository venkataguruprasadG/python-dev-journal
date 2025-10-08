"""
Coding Exercise
Write a function is_even(number) that:

Takes a single integer argument.

Returns True if the number is even, False otherwise.
"""

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(4)) # True
print(is_even(7)) # False

print("Another Method ")

def is_even_the_number(num):
    return num % 2 == 0
print(is_even_the_number(10)) # True
print(is_even_the_number(11)) # False