"""
Coding Challenge
Create a list of 4 numbers.

Insert the number 99 at the second position.

Remove and print the last element using pop().

Add [7][8][9] to the list using extend().

Find and print the index of 99.

Count how many times 7 appears.

Reverse the list and print it.
"""
num_list = [1,2,3,4]
num_list.insert(1, 99) #insert(index, element)
print(num_list.pop())
num_list.extend([7,8,9])
print(num_list.index(99)) # prints the index of 99.
print(num_list.count(7))
num_list.reverse()
print(num_list)