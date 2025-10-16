"""
Challenge:
Create a list of 5 numbers.

Add one number to the list.

Remove one number.

Print the length and the list sorted in ascending order.
"""

num_list = [1,2,3,4,5]

num_list.append(6)

num_list.remove(2)

print(len(num_list))

num_list_sort = sorted(num_list)

num_list.sort() #another method to sort the list.

print(num_list_sort)