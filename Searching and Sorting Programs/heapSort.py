def heap_sort(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
    
def heap_sort_function(arr):
    n = len(arr)

    for i in range(n // 2 -1, -1, -1):
        heap_sort(arr, n, i)
    
    for i in range(n - 1, 0 ,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_sort(arr, i, 0)

arr = [21, 5, 20,13, 10, 2]
heap_sort_function(arr)
print("Sorted array is: ",arr)

    