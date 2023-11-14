import json

contacts = {}

def add_contact():
    name = input("Enter the contact name here: ")
    number = input("Enter the contact number here: ")

    contacts[name] = number

    print(f"Contact {name} added successfully!")

def search_contact():
    name = input("Enter the name to search: ")

    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
