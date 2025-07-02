str = input("Enter a string: ")  
freq = {}

for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

max_freq = max(freq.values())

print("Maximum frequent characters: ")
for char in freq:
    if freq[char] == max_freq:
        print(char)