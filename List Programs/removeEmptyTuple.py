def remove_empty_tuples(t1):
    return [t for t in t1 if t != ()]

t1 = [(), (1, 2), (), (3), (), (4, 5)]
cleaned_list = remove_empty_tuples(t1)

print("Original Tuple: ",t1)
print("List after remove empty tuples:", cleaned_list)
