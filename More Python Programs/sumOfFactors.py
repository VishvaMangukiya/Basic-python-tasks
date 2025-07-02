import math

def min_sum_of_factors(n):
    if n <= 0:
        return 0
    
    min_sum = float('inf')  

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            pair = n // i
            current_sum = i + pair
            if current_sum < min_sum:
                min_sum = current_sum
    
    return min_sum

n = int(input("Enter a positive integer: "))
print("Minimum sum of factors:", min_sum_of_factors(n))