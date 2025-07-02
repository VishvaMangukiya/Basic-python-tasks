def congtain_vowels(word):
    vowel = set('aeiou')
    word_vowel = set(word.lower())
    return vowel.issubset(word_vowel)

user_str = input("Enter a string: ")

if congtain_vowels(user_str):
    print("The string contain all vowels")
else:
    print("The string does not contain all vowels.")