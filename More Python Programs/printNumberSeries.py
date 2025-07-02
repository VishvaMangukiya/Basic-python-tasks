def print_series(n, current=1):
    if current > n:
        return
    print(current, end=' ')
    print_series(n, current + 1)

N = int(input("Enter the value of N: "))
print("Number series from 1 to", N, ":")
print_series(N)