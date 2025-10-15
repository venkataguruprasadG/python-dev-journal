"""
Day 15: Coding Challenge - The Bank Account (State Management)
We're going to build a simple bank account class. This is a classic OOP problem because it perfectly shows how an Object manages its own internal data, or State (self.balance).

Step 1: The Blueprint (Class and Attributes)
Write the BankAccount class. It must have:

An __init__ method that accepts the owner name.

Two attributes: self.owner and self.balance (set to 0.0 initially).

Step 2: The Action (Deposit Method)
Add a method called deposit(self, amount) that:

Adds the amount to self.balance.

Prints a confirmation message like "Deposit successful. New balance: [New Balance]"
"""

"""
Your Task:

Add a method to your BankAccount class called withdraw(self, amount) that follows these rules:

Check Condition: Use an if statement to check if the amount being withdrawn is less than or equal to the self.balance.

Success: If there are sufficient funds, deduct the amount from self.balance and print a success message.

Failure: If there are insufficient funds (use an else statement), print the message: "Withdrawal failed: Insufficient funds."
"""
class bankAccount:
    def __init__(self,owner_name):
        self.owner_name = owner_name
        self.balance = 0.0
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print(f"Withdrawal failed: Insufficient funds.")
my_savings = bankAccount("Alice",)
my_savings.deposit(500)
my_savings.withdraw(200)
my_savings.withdraw(400)