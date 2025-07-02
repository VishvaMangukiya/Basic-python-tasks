def sum_of_array(arr):
    return sum(arr)

user_input = input("How many elements: ")
arr = list(map(int, user_input.split()))

result = sum_of_array(arr)
print("The sum of array is: ",result)