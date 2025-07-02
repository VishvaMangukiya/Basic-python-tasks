list1 = ['a', 'b', 'c', 'd']
list2 = [3, 1, 4, 2]

item = sorted(zip(list2, list1))

sorted_list1 = []
for i in item:
    sorted_list1.append(i[1])

print("Sorted list1 using list2:", sorted_list1)
