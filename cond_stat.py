"""Coding Exercise
Write a Python script that:

Takes an integer variable score.

Prints "Grade A" if score is 90 or above.

Prints "Grade B" if score is 75 or above but less than 90.

Prints "Grade C" if score is 60 or above but less than 75.

Prints "Fail" otherwise."""

score = 85

if score >= 90:
    print("Grade A")
elif score >= 75 and score < 90:
    print("Grade B")
elif score >= 60 and score < 75:
    print("grade C")
else:
    print("Fail")

