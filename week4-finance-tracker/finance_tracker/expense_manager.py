"""
expense_manager.py
Handles expense operations
Author: Mehak Tewari
"""

from finance_tracker.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)

    def get_all_expenses(self):
        return self.expenses

    def search_expenses(self, keyword):
        keyword = keyword.lower()
        return [
            e for e in self.expenses
            if keyword in e.category.lower() or keyword in e.description.lower()
        ]

    def category_summary(self):
        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount
        return summary

    def total_expense(self):
        return sum(e.amount for e in self.expenses)
