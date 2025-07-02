from collections import Counter

def most_frequent_char(text):
    if not text:
        return None, 0

    freq = Counter(text)

    most_common_char, count = freq.most_common(1)[0]

    return most_common_char, count

input_str = input("Enter a string: ")
char, count = most_frequent_char(input_str)

if char:
    print(f"The most frequent character is '{char}' and it appears {count} times.")
else:
    print("The input string is empty.")
