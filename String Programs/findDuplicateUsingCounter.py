from collections import Counter

s = input("Enter a string: ")

char_count = Counter(s)

duplicates = [char for char, count in char_count.items() if count > 1]

print("Duplicate characters:", duplicates)
