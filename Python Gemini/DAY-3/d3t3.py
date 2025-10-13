"""
Write a function named power_calculator that accepts two arguments: base and exponent.

Set the exponent argument to have a default value of 2.

The function should calculate base raised to the power of exponent (using the Python exponentiation operator **).

The function should return the result.

Call the function in two ways:

Once with only the base (5), and print the result.

Once with both base (5) and a custom exponent (3), and print the result.
"""

def power_calculator(base, exponent = 2):
    result = base ** exponent
    return result
print(power_calculator(5))
print(power_calculator(5, 3))