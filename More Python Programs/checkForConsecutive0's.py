def has_consecutive_zeros(number, base):

    def convert_to_base(num, base):
        if num == 0:
            return [0] 
        
        digits = []
        while num > 0:
            digit = num % base
            digits.append(digit)
            num //= base
        return digits[::-1]  

    base_representation = convert_to_base(number, base)

    for i in range(len(base_representation) - 1):
        if base_representation[i] == 0 and base_representation[i+1] == 0:
            return True

    return False

print(has_consecutive_zeros(10023, 10)) 
print(has_consecutive_zeros(10, 2))      
