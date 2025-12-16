# Contact Management System
# Week 3 Internship Project
# Author: Mehak Tewari
# Description: Manage contacts using functions and dictionaries
# Features: Add, Search, Update, Delete, Save, Load, Export

import json
import re
import csv
from datetime import datetime

DATA_FILE = "contacts_data.json"


# ---------------- VALIDATION FUNCTIONS ---------------- #

def validate_phone(phone):
    digits = re.sub(r"\D", "", phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None


def validate_email(email):
    if email == "":
        return True
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# ---------------- FILE OPERATIONS ---------------- #

def load_contacts():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("✅ No existing contacts file found. Starting fresh.")
        return {}
    except json.JSONDecodeError:
        print("⚠️ Corrupted file detected. Starting fresh.")
        return {}


def save_contacts(contacts):
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("✅ Contacts saved successfully.")


# ---------------- CRUD OPERATIONS ---------------- #

def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")

    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Phone: ")
    valid, phone = validate_phone(phone)
    if not valid:
        print("Invalid phone number!")
        return

    email = input("Email (optional): ")
    if not validate_email(email):
        print("Invalid email format!")
        return

    group = input("Group (Friends/Work/Family): ").strip() or "Other"

    contacts[name] = {
        "phone": phone,
        "email": email,
        "group": group,
        "created": datetime.now().isoformat()
    }

    print(f"✅ Contact '{name}' added.")


def search_contact(contacts):
    term = input("Search name: ").lower()
    results = {k: v for k, v in contacts.items() if term in k.lower()}

    if not results:
        print("No contacts found.")
        return

    for name, info in results.items():
        print(f"\n👤 {name}")
        print(f"📞 {info['phone']}")
        print(f"📧 {info['email']}")
        print(f"👥 {info['group']}")


def update_contact(contacts):
    name = input("Enter contact name to update: ")
    if name not in contacts:
        print("Contact not found!")
        return

    phone = input("New phone (leave blank to keep): ")
    if phone:
        valid, phone = validate_phone(phone)
        if not valid:
            print("Invalid phone!")
            return
        contacts[name]["phone"] = phone

    email = input("New email (leave blank to keep): ")
    if email:
        if not validate_email(email):
            print("Invalid email!")
            return
        contacts[name]["email"] = email

    print("✅ Contact updated.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        confirm = input("Are you sure? (y/n): ").lower()
        if confirm == "y":
            del contacts[name]
            print("✅ Contact deleted.")
    else:
        print("Contact not found!")


def display_all(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- ALL CONTACTS ---")
    for name, info in contacts.items():
        print(f"\n👤 {name}")
        print(f"📞 {info['phone']}")
        print(f"📧 {info['email']}")
        print(f"👥 {info['group']}")


def export_csv(contacts):
    with open("contacts_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Group"])
        for name, info in contacts.items():
            writer.writerow([name, info["phone"], info["email"], info["group"]])
    print("✅ Contacts exported to CSV.")


# ---------------- MAIN MENU ---------------- #

def main():
    contacts = load_contacts()

    while True:
        print("\n" + "=" * 40)
        print(" CONTACT MANAGEMENT SYSTEM ")
        print("=" * 40)
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Choose (1-7): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_all(contacts)
        elif choice == "6":
            export_csv(contacts)
        elif choice == "7":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
