matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k = int(input("Enter column number: "))

column = []
for row in matrix:
    column.append(row[k])

print("Kth column:", column)
