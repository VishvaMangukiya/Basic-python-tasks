#1st method
list = [3,7,2,10,22]
print(list)

list.clear()
print(list)

#2nd method
my_list = [11,23,1,3]
my_list[:] = []
print(my_list)

#3rd method
lst = [100,20,30,400]
del lst[:]
print(lst)

#4th method
lst1 = [20,40,60,80]
while lst1:
    lst1.pop()
print(lst1)