from itertools import permutations

dictionary = {"go", "do", "dog", "god", "dot", "got", "to"}

chars = input("Enter characters: ").lower()

possible_words = set()

for i in range(1, len(chars) + 1):
    for p in permutations(chars, i):
        word = ''.join(p)
        if word in dictionary:
            possible_words.add(word)

print("Possible words: ",possible_words)