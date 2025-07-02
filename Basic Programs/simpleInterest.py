def simple_interest(p, r, n):
    si = (p * r * n) / 100
    return si

# Example usage
print("Simple Interest\n")

p = int(input("Enter principal amount: "))
r = int(input("Enter rate of interest: "))
n = int(input("Enter number of years: "))

si = simple_interest(p, r, n)
print(f"The simple interest is: {si}")
