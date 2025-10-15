"""
Your Task: The Node Class Test
Write the Node class definition below 
(this is the same code we looked at before, but now with OOP knowledge).

Create a variable named first_node by creating a new Node object with the data value 10.

Print the data value of first_node.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
first_node = Node(10)
print(first_node.data)