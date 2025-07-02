str = input("Enter a string: ")
i = int(input("Enter the index of the character you want to remove: "))

print("The string is: ",str)
new_str = ""
for index in range(len(str)):
    if index != i:
        new_str = new_str + str[index]
print(f"After removing the {i}: {new_str}")
