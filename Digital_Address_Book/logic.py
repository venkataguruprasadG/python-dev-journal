import json
import os

try:
    with open("contacts.json","r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = []

def add_contact():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter you email address: ")
    contact = {"name": name,"phone": phone,"email": email}
    contacts.append(contact)
    print("contact is added.")

def view_contacts():
    if not contacts:
        print("There is not such contact")
    else:
        for c in contacts:
            print(f"Name: {c['name']},Phone: {c['phone']}, Email: {c['email']}")

def search_contact():
    term = input("Enter the name you want to search").lower()

    found = [c for c in contacts if term in c["name"].lower()]

    if found:
        for c in found:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print("No match found.")

def save_and_exit():
    with open("contacts.json","w") as f:
        json.dump(contacts,f, indent = 4)
    print("Contacts saved. Good Bye!")
while True:
    print("1. Add Contact")
    print("2. View all contacts")
    print("3.Search Contact")
    print("4. Exit ans save")

    choice = input("Enter your choice (1/2/3/4)")
        
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        save_and_exit()
        break
    else:
        print("Invalid choice.")