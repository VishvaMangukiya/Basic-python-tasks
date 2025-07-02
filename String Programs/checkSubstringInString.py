string = input("Enter main string: ")
substring = input("Enter substring to check: ")

if substring in string:
    print(f"Yes, '{substring}' is present in the string")
else:
    print(f"No, '{substring}' is not present in string")
