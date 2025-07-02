import json

def read_list_of_dicts(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

filename = "File Handling Programs/data.json"
list_of_dicts = read_list_of_dicts(filename)

for item in list_of_dicts:
    print(item)
