"""
Day 1: Final Test - Bringing it Together
Before we move on to Day 2's topic (Repetition and Loops), let's solidify Day 1's concepts (Variables, Operations, and Conditionals) with one final challenge.

A very common operation in Computer Science is checking for even or odd numbers, which is done using the Modulo Operator (%).

The expression A%B gives you the remainder when A is divided by B.

Example: 10%3=1 (The remainder when 10 is divided by 3 is 1)

Example: 10%2=0 (The remainder is 0, so 10 is even)

Your Final Task for Day 1:

Define a variable number and set it to any integer you like (e.g., 42).

Write a code block that checks if this number is even or odd using the modulo operator.

If the remainder when divided by 2 is 0, print: "The number is Even."

Otherwise, print: "The number is Odd."
"""

number = 42  # You can set this to any integer you like

if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")