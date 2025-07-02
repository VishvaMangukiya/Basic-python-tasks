#Iterative method
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr = [1,3,5,7,9,11,13,15]
target = int(input("Enter number to search: "))

result = binary_search_iterative(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")