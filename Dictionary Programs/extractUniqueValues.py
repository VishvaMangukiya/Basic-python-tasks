data = {
    'a': [1,2,3,4],
    'b': [4,5,6],
    'c': [4,5]
}

unique_values = set()
for val in data.values():
    unique_values.update(val)

print("Unique value: ",list(unique_values))