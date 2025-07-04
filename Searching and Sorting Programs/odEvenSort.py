def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr

arr = [34, -2, 10, 11, -9]
sorted_arr = odd_even_sort(arr)
print("Sorted array:", sorted_arr)