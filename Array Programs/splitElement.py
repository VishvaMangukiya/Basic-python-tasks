arr = list(map(int, input("Enter array elements separated by space: ").split()))
k = int(input("Enter split position: "))

def split_and_append(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

print("Resulting array:", split_and_append(arr, k))
