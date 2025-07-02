def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    pivot = arr[0]  
    left = [x for x in arr[1:] if x <= pivot]   
    right = [x for x in arr[1:] if x > pivot]  

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_arr = quick_sort(arr)

print("Sorted list:", sorted_arr)
