"""
utils.py
Utility functions
Author: Mehak Tewari
"""

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount > 0:
                return amount
            print("Amount must be positive.")
        except ValueError:
            print("Invalid number.")

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")
