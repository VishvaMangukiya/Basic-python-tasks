def largest_prime_factor(n):
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            max_prime = factor
            n //= factor
        factor += 2

    if n > 2:
        max_prime = n
    
    return max_prime

num = int(input("Enter a number:"))
print("Largest prime factor: ",largest_prime_factor(num))