def odd_in_range(n):
    for i in range(1, n):
        if (i % 2 != 0):
            print(i)
        
print("Print all odd numbers in a range\n")
n = int(input("Enter a number: "))
print("Odd numbers are: ")
odd_in_range(n)