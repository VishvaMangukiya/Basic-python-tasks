str = input("Enter a sentence: ")
k = int(input("Enter a length of k: "))

words = str.split()

print(f"Words longer than {k} characters are: ")
for word in  words:
    if len(word) > k:
        print(word)