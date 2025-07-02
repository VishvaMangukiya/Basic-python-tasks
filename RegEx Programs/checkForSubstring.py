import re

def starts_with_substring(text, substring):
    pattern = r'^' + re.escape(substring)  
    return bool(re.match(pattern, text))

text = input("Enter a string: ")
substring = input("Enter the starting substring to check: ")

if starts_with_substring(text, substring):
    print(f"Yes, the string starts with '{substring}'.")
else:
    print(f"No, the string does not start with '{substring}'.")
