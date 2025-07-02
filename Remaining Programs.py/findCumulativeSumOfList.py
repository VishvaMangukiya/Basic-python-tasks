def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total = total + num
        result.append(total)
    return result

arr = [1,2,3,4,5]
print("The Array is: ", arr)
print("Cumulative Sum:",cumulative_sum(arr))