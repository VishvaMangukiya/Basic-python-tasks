def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True  

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False  

    return arr

arr = [8, 4, 1, 56, 3, -44, 23, -6, 28]
sorted_arr = comb_sort(arr)
print("Sorted array:", sorted_arr)