matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = list(map(list, zip(*matrix)))

print("Transposed Matrix:")
for row in transpose:
    print(row)
