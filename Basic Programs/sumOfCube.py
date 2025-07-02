print("Sum of Cubes of n numbers\n")

def sum_of_cube(n):
    return sum(x * x  * x for x in range(1, n + 1))

num = int(input("Enter a number: "))
result = sum_of_cube(num)
print("Sum of cubes:", result)