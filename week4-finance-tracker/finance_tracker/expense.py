"""
expense.py
Defines the Expense class
Author: Mehak Tewari
"""

from datetime import datetime

class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = float(amount)
        self.category = category.strip().title()
        self.description = description.strip()
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
