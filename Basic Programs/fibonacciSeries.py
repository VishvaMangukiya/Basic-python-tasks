
def fibonacci_series(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(2, n):
        next = a + b
        print(next, end=" ")
        a = b
        b = next

print("Fibonacci Series:\n")

n = int(input("Enter number: "))
fibonacci_series(n)