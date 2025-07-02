def all_digits_divide_number(n):
    if n == 0:
        return False 
    
    original_num = n
    n = abs(n)  
    
    while n > 0:
        digit = n % 10
        if digit == 0:
            return False 
        if original_num % digit != 0:
            return False
        n = n // 10
    
    return True

number = int(input("Enter an integer: "))
if all_digits_divide_number(number):
    print(f"All digits of {number} divide it.")
else:
    print(f"Not all digits of {number} divide it.")