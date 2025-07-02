def sum_of_elements(list):
    mul = 1
    print(list)
    for i in list:
        mul = mul * i
    print(mul)

list = [1,2,3,5,10]
sum_of_elements(list)