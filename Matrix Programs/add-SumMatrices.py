matrix1 = [
    [5, 6, 7],
    [4, 3, 2],
    [1, 0, 9]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum_result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

sub_result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        sum_result[i][j] = matrix1[i][j] + matrix2[i][j]
        sub_result[i][j] = matrix1[i][j] - matrix2[i][j]

print("Matrix Addition:")
for row in sum_result:
    print(row)

print("\nMatrix Subtraction:")
for row in sub_result:
    print(row)
