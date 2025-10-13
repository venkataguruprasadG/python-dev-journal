"""
Write a program that uses a for loop to iterate through the numbers from 1 to 10 (inclusive).
 Inside the loop, check if each number is even or odd and print the result in this format:

For an odd number, print: "Odd: [Number]"

For an even number, print: "Even: [Number]"
"""

for i in range(1, 11):
    if i % 2 == 0:
        print(f"Even: {i}")
    else:
        print(f"Odd: {i}")