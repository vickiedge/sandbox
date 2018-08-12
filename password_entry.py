"""Vicki Edge"""

MIN_LENGTH = 5

password = input("Enter password: ")
if len(password) < MIN_LENGTH:
    print("Invalid password")
    password = input("Enter password: ")
length = len(password)
print("*" * (length))