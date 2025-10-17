"""
Write the recursive function search_bst(node, target) 
that finds a value in a Binary Search Tree ($\mathbf{O(\log N)}$ efficiency).

Base Case 1 (Found): If node.data == target, return True.
Base Case 2 (Not Found): If node is None, return False.
Recursive Step (Left): If target < node.data, recursively search the left child.
Recursive Step (Right): If target > node.data, recursively search the right child.

Show me the complete function definition. This is a crucial $O(\log N)$ algorithm! 🧠
"""

def search_bst(node, target):

    if node is None:
        return False
    
    if node.data == target:
        return True
    
    elif target < node.data:
        search_bst(node.left, target)
    elif target > node.data:
        search_bst(node.right, target)
search_bst(1,5)