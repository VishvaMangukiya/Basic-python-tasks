def negative_number(list):
    for i in list:
        if i < 0:
            print(i)

list = [10, -1, -4, 1, 5, -9]
print("Negative Numbers are:")
negative_number(list)