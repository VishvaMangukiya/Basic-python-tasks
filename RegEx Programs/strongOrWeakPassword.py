import re

def check_password_strength(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
    if re.match(pattern, password):
        return "Strong Password"
    else:
        return "Weak Password"

password = input("Enter your password: ")
print(check_password_strength(password))
