"""
Topic 2: Implementing a Binary Tree Node
A Binary Tree Node needs to store its data and two pointers: left and right.

Your Task: The Tree Node Class

Write the TreeNode class definition. It must have:

An __init__ method that accepts the data value.

The three attributes: self.data, self.left (initialized to None), and self.right (initialized to None).

Show me the complete TreeNode class definition
"""

"""
Your Task: The Inorder Traversal Function
We are going to write a recursive function to perform an Inorder Traversal.

A function inorder(node) should:

Base Case: If the current node is None, return (stop).

Recursive Step 1 (Left): Recursively call inorder() on the node.left child.

Process Data: Print the current node.data.

Recursive Step 2 (Right): Recursively call inorder() on the node.right child.
"""

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)