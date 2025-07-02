def sum_of_odd_factors(n):
    total = 0
    for i in range(1, n + 1, 2): 
        if n % i == 0:
            total += i
    return total

num = int(input("Enter a number: "))
print("Sum of odd factors of", num, "is:", sum_of_odd_factors(num))

