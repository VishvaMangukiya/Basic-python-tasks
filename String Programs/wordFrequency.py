text = "hello all how are you all hello are "
word_freq = {word: text.split().count(word) for word in set(text.split())}

print(word_freq)    