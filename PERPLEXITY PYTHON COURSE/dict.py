"""
Coding Challenge
Create a dictionary called student with keys: "name", "age", "course".

Add a new key "marks" with a numerical value.

Update "age" to a new value.

Print all keys and values.

Remove "course" using pop().

Print the updated dictionary.
"""
ex_dict = dict(name = "Vasudev Krishna", age = "25", course = "GOD")
ex_dict["marks"] = 45
ex_dict["age"] = 108
print(ex_dict.items())
ex_dict.pop("course")
print(ex_dict)