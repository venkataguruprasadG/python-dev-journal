"""
Your Task: The Node Test

Write the Node class definition as shown above.

Create a variable named first_node by creating a new Node object with the data value 10.

Print the data value of first_node.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

first_node = Node(10)

print(first_node.data)