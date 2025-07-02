def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Example usage
print("Find maximum of two numbers\n")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

maximum = find_max(a, b)
print(f"{maximum} is max")
