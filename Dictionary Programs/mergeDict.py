def merge_dict(d1,d2):
    return d1 | d2

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

merged = merge_dict(dict1,dict2)
print(merged)