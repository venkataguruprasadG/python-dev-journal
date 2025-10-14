"""
Your Task: The Insertion Test

Write the complete LinkedList class definition including the __init__ method and 
the insert_at_beginning method shown above. You will also need the Node class from before.

Create an empty Linked List named my_linked_list.

Insert the number 50 into the list.

Insert the number 100 into the list. (This makes 100 the new head).

Print the data of the head node to confirm the O(1) insertion worked.
(i.e., print the data of the new head).
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

my_linked_list = LinkedList()

print("inserting 50 at the beginning")
my_linked_list.insert_at_beginning(50)

print("inserting 100 at the beginning")
my_linked_list.insert_at_beginning(100)

print("The head node is:", my_linked_list.head.data)  # Should print 100