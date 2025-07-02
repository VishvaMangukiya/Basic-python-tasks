str = input("Enter a string: ")

special_char = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`\\"

contains_special = False

for char in str:
    if char in special_char:
        contains_special = True
        break

if contains_special:
    print("The string contains special characters.")
else:
    print("The string does NOT contain any special characters.")
