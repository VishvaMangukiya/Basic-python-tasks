list1 = [1, [], 2, [], 3, [], [4, 5], []]

updated_list = [item for item in list1 if item != []]

print("Original list: ",list1)
print("List after removing empty lists:", updated_list)
