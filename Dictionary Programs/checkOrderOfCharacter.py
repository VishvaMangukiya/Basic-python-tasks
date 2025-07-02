from collections import OrderedDict

def check_order(small, large):
    od = OrderedDict.fromkeys(large)

    index = 0
    for key in od:
        if index < len(small) and key == small[index]:
            index += 1

    return index == len(small)

small = input("Enter small string: ")
large = input("Enter large string: ")

print(check_order(small, large))  