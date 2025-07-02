def odd_even_digit_difference(number):
    num_str = str(abs(number))  
    odd_sum = 0
    even_sum = 0
    
    for digit in num_str:
        num = int(digit)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    return odd_sum - even_sum

number = int(input("Enter a number: "))
difference = odd_even_digit_difference(number)
print(f"Difference between sums of odd and even digits: {difference}")