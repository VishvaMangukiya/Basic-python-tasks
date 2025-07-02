numbers = [12, 34, 5, 7]

total = 0

for num in numbers:
    for digit in str(num):
        total += int(digit)
print("Numbers: ",numbers)
print("Sum of all digits:", total)
