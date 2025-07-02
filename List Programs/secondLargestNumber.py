num = [10,20,30,400,50]

num = list(set(num))

num.sort(reverse=True)

if len(num) >= 2:
    print("Second largest number is: ",num[1])
else:
    print("No second largest number found")