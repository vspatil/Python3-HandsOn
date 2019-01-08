#10.11

import json
filename = 'numbers2.json'
try:
    with open(filename) as file_obj:
        number = json.load(file_obj)
    #    print("my favourite number is :" + str(number))
except FileNotFoundError:
    number = int(input("Enter your favorite number: "))
    with open(filename,'w')as file_obj:
        json.dump(number,file_obj)
else:
    print("my favourite number is : " + str(number))

