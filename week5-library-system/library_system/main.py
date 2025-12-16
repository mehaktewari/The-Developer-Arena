from library_system.library import Library
from library_system.book import Book
from library_system.member import Member
from library_system.file_handler import save_data, load_data

def main():
    lib = Library()
    load_data(lib)

    while True:
        print("\n1.Add Book 2.Add Member 3.Borrow 4.Return 5.Search 6.Save & Exit")
        choice = input("Choice: ")

        if choice == "1":
            lib.add_book(Book(input("Title: "), input("Author: "), input("ISBN: ")))
        elif choice == "2":
            lib.add_member(Member(input("Name: "), input("ID: ")))
        elif choice == "3":
            print(lib.borrow_book(input("ISBN: "), input("Member ID: ")))
        elif choice == "4":
            print(lib.return_book(input("ISBN: "), input("Member ID: ")))
        elif choice == "5":
            for b in lib.search_books(input("Search: ")):
                print(b)
        elif choice == "6":
            save_data(lib)
            break

if __name__ == "__main__":
    main()
