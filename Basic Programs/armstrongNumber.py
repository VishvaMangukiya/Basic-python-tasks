def armstrong_number(num):
    n = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10

    return total == num

print("Armstrong Number\n")

num = int(input("Enter a number: "))
if armstrong_number(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
