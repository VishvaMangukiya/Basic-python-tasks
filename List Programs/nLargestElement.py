def n_largest_num(num, n):
    num = list(set(num))

    num.sort(reverse=True)

    return num[:n]

num = [20,30,99,23,100,50]
n = 3
print(n_largest_num(num, n))