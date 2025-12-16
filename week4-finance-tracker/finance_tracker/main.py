"""
main.py
Main application logic
Author: Mehak Tewari
"""

from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import save_expenses, load_expenses, backup_file
from finance_tracker.utils import get_valid_amount, get_non_empty
from finance_tracker.reports import print_category_report

def main():
    manager = ExpenseManager()

    # Load existing data
    saved = load_expenses()
    for e in saved:
        manager.add_expense(e["amount"], e["category"], e["description"])

    while True:
        print("\n" + "="*40)
        print(" PERSONAL FINANCE TRACKER ")
        print("="*40)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Category Report")
        print("5. Backup Data")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = get_valid_amount()
            category = get_non_empty("Category: ")
            description = get_non_empty("Description: ")
            manager.add_expense(amount, category, description)
            save_expenses([e.to_dict() for e in manager.get_all_expenses()])
            print("✅ Expense added")

        elif choice == "2":
            for e in manager.get_all_expenses():
                print(f"{e.date} | {e.category} | ₹{e.amount} | {e.description}")

        elif choice == "3":
            keyword = get_non_empty("Search keyword: ")
            results = manager.search_expenses(keyword)
            for e in results:
                print(f"{e.date} | {e.category} | ₹{e.amount} | {e.description}")

        elif choice == "4":
            summary = manager.category_summary()
            print_category_report(summary)

        elif choice == "5":
            backup_file()
            print("✅ Backup created")

        elif choice == "0":
            print("Thank you for using Personal Finance Tracker!")
            break

        else:
            print("Invalid choice!")
