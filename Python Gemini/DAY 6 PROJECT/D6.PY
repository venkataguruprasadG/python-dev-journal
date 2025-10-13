"""
The Project: Simple Console Contact Manager
You will create a basic system to manage a list of contacts.

Project Requirements:
Initial Data Structure: Create a global List named contacts. This list will store individual Dictionaries, where each dictionary represents a contact.

Initial Data: Add two contact dictionaries to your contacts list:

Contact 1: {"name": "Alice", "phone": "123-4567"}

Contact 2: {"name": "Bob", "phone": "987-6543"}

Function 1: add_contact(name, phone)

Takes a contact's name and phone number as arguments.

Creates a new contact dictionary using these arguments.

Appends the new dictionary to the global contacts list.

Function 2: view_contacts()

Uses a for loop to iterate over the contacts list.

Inside the loop, print the name and phone number of each contact in a clean, readable format (e.g., "Name: Alice, Phone: 123-4567").

Use an if conditional to check if the contacts list is empty, and print "No contacts found." if it is.

Your Final Task for Day 6:

Write the complete Python code for the Contact Manager, including the initial data, both function definitions, and a few lines to:

Call add_contact("Charlie", "555-1212").

Call view_contacts().
"""

contacts = []

contact1 = {"name": "Alice", "phone": "123-4567"}
contact2 = {"name": "Bob", "phone": "987-6543"}

contacts.append(contact1)
contacts.append(contact2)

def add_contact(name, phone):
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)

def view_contacts():
    for i in contacts:
        print(f"Name: {i['name']}, Phone: {i['phone']}")
    if len(contacts) == 0:
        print("No contacts found.")