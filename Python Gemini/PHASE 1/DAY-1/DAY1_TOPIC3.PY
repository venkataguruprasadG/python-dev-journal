"""
Your Task:

Let's build on our shopping cart. We need to implement a simple shipping rule:

If the total_cost is greater than 100, the shipping is free (set shipping_cost = 0).

Otherwise (if it's 100 or less), the shipping cost is fixed at 10 (set `shipping_cost = 10$).

Write the Python code block using an if statement to implement this logic, defining the shipping_cost variable inside the block.
"""

quantity = 2
price = 99.99 # This is the variable told to be taken from the previous code snippet
total_cost = price * quantity
print(total_cost)

if total_cost > 100:
    shipping_cost = 0
else:
    shipping_cost = 10