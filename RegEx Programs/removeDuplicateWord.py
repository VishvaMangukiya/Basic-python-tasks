def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = set()
    result = []

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)

    return ' '.join(result)

text = input("Enter a sentence: ")
print("After removing duplicates:", remove_duplicate_words(text))
