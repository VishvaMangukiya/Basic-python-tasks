str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

words1 = str1.split()
words2 = str2.split()

all_words = words1 + words2

uncommon = []

for word in all_words:
    if all_words.count(word) == 1:
        uncommon.append(word)

print("Uncommon words are:", uncommon)