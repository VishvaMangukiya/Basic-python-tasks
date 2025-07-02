def smallest_k_digit_number_divisible_by_X(K, X):
    smallest_K_digit = 10 ** (K - 1)
    
    if X == 0:
        return "Division by zero error"
    
    remainder = smallest_K_digit % X
    
    if remainder == 0:
        return smallest_K_digit
    else:
        return smallest_K_digit + (X - remainder)

K = int(input("Enter the number of digits (K): "))
X = int(input("Enter the divisor (X): "))
result = smallest_k_digit_number_divisible_by_X(K, X)
print(f"The smallest {K}-digit number divisible by {X} is: {result}")