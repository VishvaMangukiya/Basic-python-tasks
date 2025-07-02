text = input("Enter the string: ")
words_to_replace = input("Enter words to replace (comma-separated): ").split(',')
replacement = input("Enter replacement words (comma-separated): ").split(',')

words_to_replace = [w.strip() for w in words_to_replace]
replacement = [r.strip() for r in replacement]

words = text.split()

for i in range(len(words)):
    if words[i] in words_to_replace:
        index = words_to_replace.index(words[i])
        words[i] = replacement[index]

new_text = ' '.join(words)
print("New string:", new_text)
