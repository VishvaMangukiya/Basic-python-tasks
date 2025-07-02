def swap_first_last(lst):
    if len(lst) < 2:
        return lst
 
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

swapped_list = swap_first_last(my_list)
print("After swapping first and last:", swapped_list)
