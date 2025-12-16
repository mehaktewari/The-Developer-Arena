"""
file_handler.py
Handles file operations
Author: Mehak Tewari
"""

import json
import os
from datetime import datetime

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup"

def save_expenses(expenses):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def backup_file():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{BACKUP_DIR}/expenses_backup_{timestamp}.json"
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as src, open(backup_path, "w") as dest:
            dest.write(src.read())
