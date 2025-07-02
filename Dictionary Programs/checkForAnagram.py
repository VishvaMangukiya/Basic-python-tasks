def are_binary_anagrams(a, b):
    bin_a = bin(a)[2:]  
    bin_b = bin(b)[2:]

    return sorted(bin_a) == sorted(bin_b)

a = 20
b = 20
print(are_binary_anagrams(a, b)) 
