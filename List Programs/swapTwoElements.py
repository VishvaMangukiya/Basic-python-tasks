def swap_elements(lst, pos1, pos2):
    if pos1 < 0 or pos1 >= len(lst) or pos2 < 0 or pos2 >= len(lst):
        return lst
    
    lst[pos1], lst[pos2] = lst[pos2], lst[1]
    return lst

my_list = [1,2,3,4,5,6]
print("Original list: ",my_list)

swapped_list = swap_elements(my_list, 2, 3)
print("After swapping position 2 and 3: ",swapped_list)