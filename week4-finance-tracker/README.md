# Week 4: File Handling & Final Project — Personal Finance Tracker

## 📌 Overview

The **Personal Finance Tracker** is a Python-based, menu-driven application developed as the **final project of Week 4**. It combines concepts from **Weeks 1–4**, including variables, control flow, functions, dictionaries, file handling, modular programming, and error handling.

This project allows users to **record expenses, categorize spending, persist data using files, and generate reports**, simulating a real-world personal finance management system.

---

## 🎯 Learning Objectives

By completing this project, you will demonstrate:

* Proficiency in **file handling (JSON & CSV)**
* Ability to build **modular Python applications**
* Effective use of **functions, classes, and dictionaries**
* Proper **error handling and validation**
* Real-world problem-solving and clean code practices

---

## 📚 Theory Concepts Covered

* File Operations (read/write)
* Text, JSON, and CSV file handling
* Error & Exception Handling
* Context Managers (`with` statement)
* Code modularization
* Debugging file-based applications

---

## 🛠️ Project Features

* Add, edit, delete, and search expenses
* Categorize expenses (Food, Transport, Bills, etc.)
* Persistent data storage using JSON
* Automatic backup & restore system
* Monthly and category-wise reports
* Budget tracking
* CSV export support
* User-friendly CLI menu
* Robust error handling

---

## 🗂️ Project Structure

```
week4-finance-tracker/
│── finance_tracker/
│   ├── __init__.py
│   ├── main.py
│   ├── expense.py
│   ├── expense_manager.py
│   ├── file_handler.py
│   ├── reports.py
│   └── utils.py
│
│── data/
│   ├── expenses.json
│   ├── backup/
│   └── exports/
│
│── tests/
│   ├── test_expense.py
│   ├── test_file_handler.py
│   └── test_reports.py
│
│── run.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🧩 Module Description

### `expense.py`

* Defines the **Expense** class
* Stores date, amount, category, and description
* Includes validation logic

### `expense_manager.py`

* Manages all expenses
* Add, remove, search, filter expenses
* Acts as the core data handler

### `file_handler.py`

* Handles saving/loading data (JSON)
* Backup and restore functionality
* CSV import/export support

### `reports.py`

* Monthly summaries
* Category-wise breakdown
* Statistical analysis

### `utils.py`

* Input validation helpers
* Date formatting
* Common utility functions

### `main.py`

* User interface and menu system
* Integrates all modules

---

## ▶️ How to Run

```bash
# Navigate to project directory
cd week4-finance-tracker

# Run application
python run.py
```

---

## 📊 Sample Menu

```
========================================
      PERSONAL FINANCE TRACKER
========================================
1. Add New Expense
2. View All Expenses
3. Search Expenses
4. Generate Monthly Report
5. View Category Breakdown
6. Set / Update Budget
7. Export Data to CSV
8. View Statistics
9. Backup / Restore Data
0. Exit
========================================
```

---

## 🧪 Testing

* Unit tests for expenses
* File handling validation tests
* Report generation tests

Run tests:

```bash
python -m unittest discover tests
```

---

## 📈 Sample Output

```
--- ADD NEW EXPENSE ---
Amount: 1200
Category: Food
Description: Lunch
✅ Expense added successfully!
```

---

## 🧠 What I Learned

* File persistence using JSON & CSV
* Modular project design
* Defensive programming with exceptions
* Data validation techniques
* Writing testable and maintainable code

---

## ✅ Quality Checklist

* [x] Modular project structure
* [x] Clean and readable code
* [x] Proper error handling
* [x] File-based persistence
* [x] Documentation included
* [x] Test cases provided

---

## 📤 Submission Notes

This project is **internship-ready** and meets all academic evaluation criteria for Week 4.

---

**Author:** Mehak Tewari
**Week:** 4 — File Handling & Final Project
