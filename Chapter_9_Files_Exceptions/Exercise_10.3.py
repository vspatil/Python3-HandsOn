#10.3
"""
text = input("Please enter your name: ")
with open ("C:\\Users\Vani\Desktop\write.txt",'w') as file:
    file.write(text)

"""
#10.4

"""
text = ''
while text != 'quit':
    text = input("Enter youe name :")
    if text == 'quit':
        break
    else:
        text1 = "Hello " + text
        print(text1)
    with open ("C:\\Users\Vani\Desktop\write.txt",'a') as file:
        file.write(text + " visited!" + "\n")

"""

#10.5

text = ""

while text !='quit':
    text = input(" Why you like programming ? ")
    if text == 'quit':
        break
    else:
        with open("C:\\Users\Vani\Desktop\Responses.txt",'a') as file:
            file.write(text.title() + "\n")