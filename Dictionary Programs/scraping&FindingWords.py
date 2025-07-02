words = input("Enter words saperated by space: ").split()
ordered = []

for w in words:
    if w == ''.join(sorted(w)) and len(w) > 1:
        ordered.append(w)

print(ordered)