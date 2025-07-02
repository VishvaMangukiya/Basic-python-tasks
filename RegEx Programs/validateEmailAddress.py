import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
