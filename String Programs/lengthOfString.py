str = "Hello Good Morning..!"

#1st method
length = len(str)
print("Length: ",length)

#2nd method
count = 0
for char in str:
    count += 1
print("Length: ", count)

#3rd method
count = 0
try:
    while str[count]:
        count = count + 1
except IndexError:
    pass
print("Length: ", count)

#4th method
def str_len(str):
    if str == '':
        return 0
    else:
        return 1 + str_len(str[1:])
    
print("Length: ",str_len(str))