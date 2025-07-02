
seen = ""

for char in str1:
    if char not in seen:
        result += char
        seen += char
    else:
        result += '*'