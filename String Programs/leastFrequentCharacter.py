str = input("Enter a string: ")  
freq = {}

for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

min_freq = min(freq.values())

print("Least frequent characters: ")
for char in freq:
    if freq[char] == min_freq:
        print(char)