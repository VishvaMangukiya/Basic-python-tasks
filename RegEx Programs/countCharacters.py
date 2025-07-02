import re

def count_characters(text):
    uppercase = len(re.findall(r'[A-Z]', text))
    lowercase = len(re.findall(r'[a-z]', text))
    digits = len(re.findall(r'[0-9]', text))
    special = len(re.findall(r'[^a-zA-Z0-9]', text))

    return uppercase, lowercase, digits, special

string = input("Enter a string: ")

upper, lower, digit, special = count_characters(string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
print(f"Digits: {digit}")
print(f"Special characters: {special}")