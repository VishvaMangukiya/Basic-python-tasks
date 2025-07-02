import re

def ends_with_alphanumeric(text):
    pattern = r'[A-Za-z0-9]$'  
    return bool(re.search(pattern, text))

string = input("Enter a string: ")

if ends_with_alphanumeric(string):
    print("Yes, the string ends with an alphanumeric character.")
else:
    print("No, it does not end with an alphanumeric character.")
