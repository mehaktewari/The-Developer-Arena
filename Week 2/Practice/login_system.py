username = "admin"
password = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("✅ Login Successful!")
else:
    print("❌ Invalid Credentials!")
