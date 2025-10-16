"""
Coding Challenge
Create a variable user_age and assign it an integer.

Use an if-elif-else statement to print:

"Child" if age < 13

"Teenager" if 13 <= age < 20

"Adult" if 20 <= age < 65

"Senior" if age >= 65
"""
user_age = 25
if user_age < 13:
    print("Child")
elif 13 <= user_age < 20:
    print("Teenager")
elif 20 <= user_age < 65:
    print("Adult")
elif user_age >= 65:
    print("Senior") 