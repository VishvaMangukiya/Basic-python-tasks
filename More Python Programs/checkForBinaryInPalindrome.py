def is_binary_palindrome(n):
    binary_str = bin(n)[2:]  
    return binary_str == binary_str[::-1]

number = int(input("Enter a number: "))
if is_binary_palindrome(number):
    print(f"The binary representation of {number} is a palindrome.")
else:
    print(f"The binary representation of {number} is not a palindrome.")
