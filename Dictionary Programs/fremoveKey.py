#1st method
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']
print(my_dict) 

#2nd method
my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_value = my_dict.pop('b')
print(my_dict)       

#3rd method
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.popitem()
print(my_dict) 
