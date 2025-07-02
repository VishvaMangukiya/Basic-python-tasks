def check_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False
    
    return increasing or decreasing

arr = [1,2,2,3,4,4]
print(f"{arr}-Monotonic? ",check_monotonic(arr))

arr2 = [1,2,8,3]
print(f"{arr2}-Monotonic?",check_monotonic(arr2))

arr3 = [7,7,6,6,5,4,3]
print(f"{arr3}-Monotonic?",check_monotonic(arr3))


