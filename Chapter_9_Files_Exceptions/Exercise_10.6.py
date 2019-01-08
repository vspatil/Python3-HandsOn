#10.6,#10.7
"""
while True:
    num1 = input("Please enter the first number: ")
    if num1 == 'q':
        break
    num2 = input("Please enter the second number: ")
    if num2 == 'q':
        break
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print(" Please enter integers!")
    else:
        print(answer)

"""
#10.8
"""
def read_files(filenames):
    try:
        with open(filenames,'r') as file_object:
            contents = file_object.readlines()
    except FileNotFoundError:
        pass
            #print(" Sorry the file is not found!")
    else:
        print(contents)

filenames =["C:\\Users\Vani\Desktop\dogs.txt"]
#for filename in filenames:
    #print(filename)
read_files(str("C:\\Users\Vani\Desktop\Cas.txt"))
"""

#10.10

def count_words(filename):
    try:
        with open(filename,'r')as file_object:
            contents = file_object.read().rstrip()
            print(contents)
    except FileNotFoundError:
        print("Sorry File os not foumd!")
    else:
         contents = str(contents.count('dog'))
         #print(str(content.count('dog')))
        #print(contents)
         print("The word dog appears " + str(contents) + " times")



filenames =["C:\\Users\Vani\Desktop\dgs.txt"]
#for filename in filenames:
    #print(filename)
count_words(str("C:\\Users\Vani\Desktop\cats.txt"))