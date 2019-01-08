#10.1
"""
#filename = "C:\\Users\Vani\Desktop\learning_python.txt"
with open("C:\\Users\Vani\Desktop\learning_python.txt") as file_object:
    #contents = file_object.read()
    #print(contents.rstrip())

 lines = file_object.readlines()
for line in lines:
print(line.rstrip())

"""
#10.2

with open('C:\\Users\Vani\Desktop\learning_python.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        #line.replace('python','c')
        print(line.replace('python','c').rstrip())
