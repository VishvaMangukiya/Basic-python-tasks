def count_occurrences(lst1, element):
    return lst1.count(element)

lst1 = [1, 2, 3, 4, 2, 2, 5]
element = 2
print("Original list: ",lst1)
print(f"{element} appears {count_occurrences(lst1, element)} times.")