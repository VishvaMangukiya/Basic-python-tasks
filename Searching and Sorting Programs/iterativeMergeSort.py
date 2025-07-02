def merge_sort(arr):
    n = len(arr)
    size = 1
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(start + size, n)
            end = min(start + 2 * size, n)
            left = arr[start:mid]
            right = arr[mid:end]
            arr[start:end] = sorted(left + right)
        size *= 2
    return arr

arr = list(map(int, input("Enter numbers: ").split()))
print("Sorted:", merge_sort(arr))
