data = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
grouped = {}

for tup in data:
    key = tup[0]
    if key not in grouped:
        grouped[key] = list(tup[1:])
    else:
        grouped[key].extend(tup[1:])

result = [(key, *value) for key, value in grouped.items()]
print(result)