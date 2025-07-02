def rotate_left(arr, k):
    n = len(arr)
    k = k % n  
    return arr[k:] + arr[:k]

arr = list(map(int, input("Enter array elements separated by space: ").split()))
k = int(input("Enter number of positions to rotate left: "))

rotated = rotate_left(arr, k)
print("Rotated array:", rotated)
