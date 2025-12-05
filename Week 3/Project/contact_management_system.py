# -------------------------------
# Contact Management System
# -------------------------------

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.\n")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}\n")
    else:
        print("Contact not found.\n")

# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\n---- Contact List ----")
    for name, phone in contacts.items():
        print(f"{name} : {phone}")
    print("-----------------------\n")

# Main program loop
def main():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)

        elif choice == "2":
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == "3":
            display_contacts()

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1–4.\n")

# Run the program
if __name__ == "__main__":
    main()
