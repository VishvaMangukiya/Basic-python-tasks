data = {'banana': 3, 'apple': 5, 'orange': 2}

#sort by key
sorted_by_key = dict(sorted(data.items()))
print(sorted_by_key) 

#sort by value
sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_by_value)