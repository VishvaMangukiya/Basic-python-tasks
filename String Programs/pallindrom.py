def check_pallindrom(str):
    reverse_str = ''.join(reversed(str))
    if str == reverse_str:
        print(f"The string '{str}' is pallindrom")
    else:
        print(f"The string '{str}' is not pallindrom")

str = input("Enter a string: ")
print("Original String: ",str)
check_pallindrom(str)      
        
    