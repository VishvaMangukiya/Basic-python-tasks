str = input("Enter a string: ")

is_binary = True
for char in str:
    if char != '0' and char != '1':
        is_binary = False
        break

if is_binary:
    print("The string is a binary string.")
else:
    print("The string is NOT a binary string.")
