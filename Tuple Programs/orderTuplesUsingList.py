data = [('apple', 3), ('banana', 1), ('cherry', 2), ('Mango', 4)]
order = ['Mango', 'banana', 'cherry', 'apple']

sorted_data = sorted(data, key=lambda x: order.index(x[0]))

print("Ordered tuples:", sorted_data)
