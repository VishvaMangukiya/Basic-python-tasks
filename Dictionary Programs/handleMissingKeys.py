data = {'a': 1, 'b': 2}

try:
    print(data['a'])
except KeyError:
    print("Key not found")
