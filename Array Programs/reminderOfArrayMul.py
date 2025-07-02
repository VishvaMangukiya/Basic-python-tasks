def find_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

arr = list(map(int, input("Enter array elements separated by space: ").split()))
n = int(input("Enter divisor (n): "))
 
print("Remainder of array multiplication divided by n:", find_remainder(arr, n))
