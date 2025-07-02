tuple_of_lists = ([1, 2], [3, 4], [5, 6])
flattened = tuple(item for sublist in tuple_of_lists for item in sublist)

print(flattened)
