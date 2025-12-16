# Basic test file for Contact Management System

from contacts_manager import validate_phone, validate_email

print(validate_phone("+1 234 567 8900"))   # Expected: True
print(validate_phone("123"))               # Expected: False

print(validate_email("test@example.com"))  # Expected: True
print(validate_email("wrong-email"))       # Expected: False
