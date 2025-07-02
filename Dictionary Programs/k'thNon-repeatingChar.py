from collections import OrderedDict

def kth_non_repeating_char(s, k):
    char_count = OrderedDict()
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1

    non_repeating = [ch for ch in char_count if char_count[ch] == 1]

    if k <= len(non_repeating):
        return non_repeating[k-1]
    else:
        return "Less than K non-repeating characters"

s = "gooff"
k = 1
print(kth_non_repeating_char(s, k))  
