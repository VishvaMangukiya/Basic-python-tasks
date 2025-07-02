def print_duplicates(numbers):
    duplicates = []

    for i in numbers:
        if numbers.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    print("Original list: ",my_list)
    print("Duplicate elements are:", duplicates)

my_list = [1, 2, 3, 2, 4, 5, 1, 6]
print_duplicates(my_list)
