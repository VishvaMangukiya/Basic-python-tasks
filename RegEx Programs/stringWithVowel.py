import re

def starts_with_vowel(text):
    pattern = r'^[aeiouAEIOU]'
    return bool(re.match(pattern, text))

string = input("Enter a string: ")

if starts_with_vowel(string):
    print("Yes, the string starts with a vowel.")
else:
    print("No, the string does not start with a vowel.")
