"""
💪 Coding Challenge
Task:

Create three variables: math_score, science_score, and english_score with integer values.

Check if all three scores are greater than or equal to 40 (pass mark).

Use logical operators to verify if the student passed all subjects.

Print a message:

"Passed all subjects!" if all scores are >= 40.

Otherwise, "Needs improvement."

💡 Hint: Create a boolean expression using and.
"""

math_score = 85
science_score = 90
english_score = 80

if math_score >= 40 and science_score >= 40 and english_score >= 40:
    print("Passed all Subjects")
else:
    print("Needs Improvement")