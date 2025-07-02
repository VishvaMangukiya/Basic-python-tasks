import math

def number_of_stopping_stations(S, N):
    if S < N:
        return 0
    if N < 2:
        return 0
    return math.comb(S - 2, N - 2)

S = int(input("Enter total number of stations (S): "))
N = int(input("Enter number of stopping stations (N): "))
result = number_of_stopping_stations(S, N)
print(f"Number of ways to choose stopping stations: {result}")