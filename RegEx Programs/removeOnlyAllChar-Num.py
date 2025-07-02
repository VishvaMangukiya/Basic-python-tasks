import re

def remove_special_characters(text):
    return re.sub(r'[^A-Za-z0-9]', '', text)

string = input("Enter a string: ")
cleaned = remove_special_characters(string)
print("New string:", cleaned)
