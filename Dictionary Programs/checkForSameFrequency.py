from collections import Counter

def check_frequency(s):
    freq = Counter(Counter(s).values())
    return (
        len(freq) == 1 or
        (len(freq) == 2 and (
            1 in freq and freq[1] or
            abs(*freq.keys()) == 1 and 1 in freq.values()
        ))
    )

s = input("Enter a string: ")
print(check_frequency(s))