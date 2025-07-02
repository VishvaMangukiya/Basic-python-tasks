def positive_number(list):
    for i in list:
        if i > 0:
            print(i)

list = [3, -3, 4, 9, -10, 11]
print("Positive Numbers are:")
positive_number(list)