shopping_list = []

while True:
    print("\n🛒 Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found.")
    elif choice == "3":
        print("Your List:", shopping_list)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
