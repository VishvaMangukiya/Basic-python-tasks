my_dict = my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}

value = int(input("Enter vlaue you want to access: "))

result = []

for key, val in my_dict.items():
    if val == value: 
        result.append(key)

print("Keys with value ",value, ": ",result)