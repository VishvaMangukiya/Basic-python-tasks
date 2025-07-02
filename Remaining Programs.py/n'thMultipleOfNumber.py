def find_nth_multiple_in_fibonacci(k, n):
    a, b = 0, 1
    count = 0

    while True:
        if a % k == 0:
            count += 1
            if count == n:
                return a
        a, b = b, a + b

k = 3
n = 5
result = find_nth_multiple_in_fibonacci(k, n)
print(f"The {n}th multiple of {k} in Fibonacci series is: {result}")
