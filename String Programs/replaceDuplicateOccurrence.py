str1 = input("Enter a string: ")
result = ""
seen = ""

for char in str1:
    if char not in seen:
        result += char
        seen += char
    else:
        result += '*'

print("New string:", result)
