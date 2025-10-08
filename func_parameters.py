"""Coding Exercise
Write a function calculate_area(length, width=10) that:

Returns the area of a rectangle.

If width is not provided, assumes it as 10.

Test with:

Only one argument.

Two arguments."""

def calculate_area(length, width=10):
    return length * width
print(calculate_area(5))     # Should use default width of 10, output: 50
print(calculate_area(5,width = 4)) # Should use provided width of 4, output: 20

