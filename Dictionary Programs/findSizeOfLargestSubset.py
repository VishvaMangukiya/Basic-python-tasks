from collections import Counter

def largest_anagram_group(words):
    signatures = [''.join(sorted(word)) for word in words]
    
    count = Counter(signatures)

    return max(count.values())

words = ["bat", "tab", "cat", "act", "tac", "tap"]
print(largest_anagram_group(words))  