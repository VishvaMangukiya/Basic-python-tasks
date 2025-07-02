str = input("Enter a string: ")
i = int(input("Enter the index of the character to remove:"))

if 0 <= i < len(str):
    new_str = str[:i] + str[i+1:]
    print("String after removing character at index", i, ":", new_str)
else:
    print("Invalid index!")