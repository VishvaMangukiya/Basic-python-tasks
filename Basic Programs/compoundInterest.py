def compound_interest(p, r, t):
    amount = p * pow((1 + r / 100), t)
    ci = amount - p
    return ci

print("Compound Interest\n")

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest (% per period): "))
t = int(input("Enter number of periods: "))

ci = compound_interest(p, r, t)
print(f"The Compound Interest is: {ci:.2f}")
