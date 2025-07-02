from itertools import permutations

s = input("Enter a string: ")

perm_list = permutations(s)

for perm in perm_list:
    print(''.join(perm))
