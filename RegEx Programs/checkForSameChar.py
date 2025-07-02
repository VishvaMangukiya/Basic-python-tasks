import re

def start_and_ends_same(s):
    pattern = r'^(.).*\1$'
    return bool(re.match(pattern, s))

string = input("Enter a string: ")

if start_and_ends_same(string):
    print("Yes, the string starts and ends with the same character.")
else:
    print("Np, the string does not start nd ends with the same character.")