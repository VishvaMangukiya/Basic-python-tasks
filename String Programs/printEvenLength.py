str = "Hello, all Good Morning student..!"

words = str.split()

print("Even length words are: ")
for word in words:
    if len(word) % 2 == 0:
        print(word)

