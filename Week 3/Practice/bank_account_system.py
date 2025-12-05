account = {"balance": 0}

def deposit(amount):
    account["balance"] += amount
    return account["balance"]

def withdraw(amount):
    if amount > account["balance"]:
        return "Insufficient balance"
    account["balance"] -= amount
    return account["balance"]

def check_balance():
    return account["balance"]

# Test
print("Deposit:", deposit(500))
print("Withdraw:", withdraw(200))
print("Balance:", check_balance())
