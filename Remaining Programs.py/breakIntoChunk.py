def chunk_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
result = chunk_list(my_list, chunk_size)
print(result)
