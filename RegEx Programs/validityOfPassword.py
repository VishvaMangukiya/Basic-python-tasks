import re

def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
    return bool(re.match(pattern, password))

password = input("Enter password: ")

if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")
