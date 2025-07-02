s = input("Enter a string: ")
n = int(input("Enter number of characters to rotate by: "))

left_rotated = s[n:] + s[:n]
print("Left rotated string:", left_rotated)

right_rotated = s[-n:] + s[:-n]
print("Right rotated string:", right_rotated)
