def sum_of_even_factors(n):
    if n <= 0:
        return 0
    
    sum_even = 0
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum_even += i
            if (n // i) % 2 == 0 and (n // i) != i:
                sum_even += n // i
                
    return sum_even

number = int(input("Enter a positive integer: "))
result = sum_of_even_factors(number)
print(f"Sum of even factors of {number} is: {result}")