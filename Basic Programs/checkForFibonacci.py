def fibonacci_number(n):
    temp = 0
    first = 1
    second = 1

    if n == 0 or n == 1:
        return True
    else:
        while temp < n:
            temp = first + second
            second = first
            first = temp
        return temp == n

print("Check for Fibonacci number\n")
n = int(input("Enter number: "))

if fibonacci_number(n):
    print("The number is a Fibonacci number")
else:
    print("The number is not a Fibonacci number")
