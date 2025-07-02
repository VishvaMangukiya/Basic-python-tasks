import math

def num_solutions_modular_equation(a, b, m):
    d = math.gcd(a, m)
    
    if b % d != 0:
        return 0 
    else:
        return d  

a = 14
b = 30
m = 100

solutions = num_solutions_modular_equation(a, b, m)
print(f"Number of solutions to {a}x ≡ {b} (mod {m}) is: {solutions}")