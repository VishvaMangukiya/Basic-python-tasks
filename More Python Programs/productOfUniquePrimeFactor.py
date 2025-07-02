def product_of_unique_prime_factors(n):
    product = 1
    if n % 2 == 0:
        product *= 2
        while n % 2 == 0:
            n //= 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            product *= i
            while n % i == 0:
                n //= i
        i += 2

    if n > 2:
        product *= n

    return product

num = int(input("Enter a number: "))
print("Product of unique prime factors:", product_of_unique_prime_factors(num))
