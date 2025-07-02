def group_anagrams(word_list):
    anagram_dict = {}

    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    for group in anagram_dict.values():
        print(group)

words = ["bat", "tab", "eat", "tea", "tan", "nat", "ate"]
group_anagrams(words)
