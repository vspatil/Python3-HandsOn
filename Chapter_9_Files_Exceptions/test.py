import json
filename = 'numbers.json'
with open(filename) as file_obj:
    number = json.load(file_obj)
    print("my favourite number is :" + number)