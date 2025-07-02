def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

arr = [10, 4, 99, 23, 8]
print("Largest element is:", find_largest(arr))

