def print_z_form(matrix):
    n = len(matrix)
    
    for i in range(n):
        print(matrix[0][i], end=" ")
    print()
    
    for i in range(1, n-1):
        for j in range(n):
            if i + j == n - 1:
                print(matrix[i][j], end=" ")
                break
        print()

    for i in range(n):
        print(matrix[n-1][i], end=" ")
    print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix in Z form:")
print_z_form(matrix)