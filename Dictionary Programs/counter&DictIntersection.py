from collections import Counter

def can_form_string(a, b):
    count_a = Counter(a)
    count_b = Counter(b)

    return count_b & count_a == count_b

A = input("Enter characters: ")
B = input("Enter characters to check: ")
print(can_form_string(A, B))  


