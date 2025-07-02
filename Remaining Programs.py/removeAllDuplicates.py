def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

sentence = "I am learning Python And also learning PHP"
print(remove_duplicate_words(sentence))
