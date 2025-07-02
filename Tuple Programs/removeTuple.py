data = [(1, 2), (3,), (4, 5, 6), (7,)]
k = int(input("Enter length of tuple to remove: "))

new_tuple = [tup for tup in data if len(tup) != k]

print("Updated tuples:", new_tuple)
