list1 = [10,20,30,40,50,100]

found = False
for i in list1:
    if i == 20:
        found = True
        break
if found:
    print("Element Exists..!")
else:
    print("Element not Exists..!")
