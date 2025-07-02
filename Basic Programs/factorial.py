def factorial(n):
    if n < 0:
        return None 
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("Factorial\n")
n = int(input("Enter a number: "))

result = factorial(n)
print(f"The factorial of {n} is {result}")

