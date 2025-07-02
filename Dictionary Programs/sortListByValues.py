from operator import itemgetter

data = [
    {'name': 'Raj', 'age': 25},
    {'name': 'Jay', 'age': 19},
    {'name': 'Nisha', 'age': 30}
]

#sorting in ascending order
sorted_data = sorted(data, key=itemgetter('age'))
print(sorted_data)

#sorting in descending order
sorted_data = sorted(data, key=itemgetter('age'), reverse=True)
print(sorted_data)

#sort by multiple keys
sorted_data = sorted(data, key=itemgetter('age', 'name'))
print(sorted_data)

#using lambda function
sorted_people = sorted(data, key=lambda x: x['age'])
