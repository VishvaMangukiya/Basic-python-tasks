def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, d):
    n = len(arr)
    if d == 0 or d == n:
        return
    
    reverse(arr, 0, d - 1)

    reverse(arr, d, n - 1)
    
    reverse(arr, 0, n - 1)

arr = [1, 2, 3, 4, 5, 6]
d = 3
left_rotate(arr, d)
print("Rotated array: ",arr)
    