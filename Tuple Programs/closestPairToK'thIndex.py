data = [(4, 7), (2, 6), (9, 8), (1, 5), (3, 5)]
k = int(input("Enter index to compare: "))
target = int(input("Enter target number: "))

closest_tuple = min(data, key=lambda x: abs(x[k] - target))

print("Closest tuple:", closest_tuple)
