tuple1 = (1, 2)
tuple2 = (3, 4)

result = []

for i in tuple1:
    for j in tuple2:
        result.append((i, j))

print(result)
