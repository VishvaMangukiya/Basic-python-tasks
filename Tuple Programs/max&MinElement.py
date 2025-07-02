my_tuple = input("Enter multiple values saperated by space: ").split()
my_tuple = tuple(map(int, my_tuple))

k = int(input("Enter how many element you want: "))

min_k = sorted(my_tuple)[:k]

max_k = sorted(my_tuple, reverse=True)[:k]

print(f"Minimum {k} elements:", min_k)
print(f"Maximum {k} elements:", max_k)
