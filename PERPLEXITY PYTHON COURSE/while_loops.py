"""
Coding Challenge:
Use a while loop to print numbers from 10 down to 1.

Use break to exit the loop early if the number reaches 5.

Inside the loop, skip printing the number 8 using continue.
"""
num = 10
while num >= 1:
    if num == 5:
        break
    if num == 8:
        num -= 1
        continue
    print(num)
    num -= 1