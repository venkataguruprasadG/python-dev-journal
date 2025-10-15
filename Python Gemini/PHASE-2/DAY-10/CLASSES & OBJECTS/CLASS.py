"""
Your Task: The Object Test

Write the User class definition shown above.

Create a new User object named admin_user with the name "Jane Doe" and email "jane@example.com".

Print the email attribute of the admin_user object.
"""

class user:
    def __init__(self,name,email):
        self.name = name
        self.email = email
admin_user = user("Jane Doe","jane@emxample.com")

"""
Your Task - Object Creation and Access
Write the complete Car class definition shown above.

Create a new Car object named my_first_car and set its color to "green" and its model to "Honda".

Write the line of code to print only the model of my_first_car
"""

class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model
my_first_car = Car("green","honda")
print(my_first_car.model)