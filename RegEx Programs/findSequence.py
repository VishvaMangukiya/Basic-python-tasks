import re

def find_capitalized_words(text):
    pattern = r'\b[A-Z][a-z]+'

    matches = re.findall(pattern, text)
    return matches

text = input("Enter a string: ")
result = find_capitalized_words(text)

print("Matched sequences:", result)
