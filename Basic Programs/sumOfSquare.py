print("Sum of Squares of n numbers\n")

def sum_of_squares(n):
    return sum(x * x for x in range(1, n + 1))

num = int(input("Enter a number: "))
result = sum_of_squares(num)
print("Sum of squares:", result)
