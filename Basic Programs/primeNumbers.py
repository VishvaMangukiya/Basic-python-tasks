def primes_range(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for n in range(start, end + 1):
        if n > 1:  
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                print(n)

# Example usage
print("Prime numbers in interval\n")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
primes_range(num1, num2)
