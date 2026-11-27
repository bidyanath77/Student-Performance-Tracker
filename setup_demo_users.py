
import getpass

from auth import register_user

print("Student Performance Tracking System")
print("Create a local login account")
print()

username = input("Enter username: ").strip()
password = getpass.getpass("Enter password (minimum 12 characters): ")

if register_user(username, password):
    print("Account created successfully!")
    print("You can now log in to the application.")
else:
    print("Account creation failed.")
    print("Check the username, password length, or whether the username already exists.")
