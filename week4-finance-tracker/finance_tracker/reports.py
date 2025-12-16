"""
reports.py
Generates reports
Author: Mehak Tewari
"""

def monthly_report(expenses):
    report = {}
    for e in expenses:
        month = e["date"][:7]
        report[month] = report.get(month, 0) + e["amount"]
    return report

def print_category_report(summary):
    print("\n--- CATEGORY WISE EXPENSE ---")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")
