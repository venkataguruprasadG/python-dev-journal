"""
Coding Challenge
Create and open a file "data.txt" for writing.

Write three lines of text (can be anything).

Close the file.

Open the file for reading, and print each line.
"""

file = open("data.txt","w")
file.write("hello World!!!")
file.close()

file = open("data.txt","r")
for line in file:
    print(line.strip())