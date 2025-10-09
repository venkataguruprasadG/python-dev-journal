"""Coding Exercise
Write a function display_user_info(**info) that:

Accepts any number of named attributes.

Prints each attribute in "key: value" format.

Call it with different sets of user info, e.g., name, age, email."""

def dsiplay_user_info(**info):
    for key,value in info.items():
        print(f"{key}: {value}")
print(dsiplay_user_info(name="Alice", age=30))