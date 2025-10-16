"""
💪 Coding Challenge
Task:

Create two variables: one integer (num1) and one float (num2).

Perform all seven arithmetic operations between them (+, -, *, /, //, %, **) and print the results.

Then, convert the result of division to an integer using int().

Finally, print the type of each operation’s result using type().
"""

num1 = 12
num2 = 5.0

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

result = num1 / num2
result_int = int(result)
print(type(result))
print(type(result_int))