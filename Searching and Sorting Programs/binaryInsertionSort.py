def binary_search(arr, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr

arr = [37, 23, 0, 17, 12, 72, 31]
sorted_arr = binary_insertion_sort(arr)
print("Sorted array:", sorted_arr)