def positive_in_range(first, end):
    for i in range(first, end + 1):
        if (i > 0):
            print(i)

print("Print all positive numbers in a range\n")
first = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Positive numbers are: ")
positive_in_range(first, end)