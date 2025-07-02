def sort_dict_key_and_values(data):
    for key in data:
        data[key].sort()

    return dict(sorted(data.items()))

data = {
    'banana': [3, 1, 2],
    'apple': [9, 5, 6],
    'orange': [7, 4, 8]
}

sorted_result = sort_dict_key_and_values(data)
print(sorted_result)
