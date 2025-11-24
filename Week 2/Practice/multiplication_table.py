num = int(input("Enter number for multiplication table: "))

print(f"\n📊 Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
