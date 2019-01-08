"""prompt = "Enter a series of toppings : "

message = ""
while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("We will add " + message + " to the pizza!")"""
"""
age=''
while age != 'quit':
    age = input("Enter your age : ")
    if age == 'quit':
        break
    elif age < 3:
        print("The ticket is free!")
    elif age > 3 and age < 12:
        print("The ticket costs $10!")
    else:
        print("The ticket costs $15!")
"""
#using condition in the while stmt
"""age=''
while age != 'quit':
    age = input("Enter your age : ")
    if age == 'quit':
        break
    elif age <= 3:
        print("The ticket is free!")
    elif age > 3 and age <= 12:
        print("The ticket costs $10!")
    elif age > 12 :
        print("The ticket costs $15!")"""

#Using active variable to control the loop
"""active = True
while active:
    age = input("Enter your age : ")
    if age == 'quit':
        active = False
    elif age <= 3:
        print("The ticket is free!")
    elif age > 3 and age <= 12:
        print("The ticket costs $10!")
    else:
        print("The ticket costs $15!")"""

#using break stmt to exit the loop
"""
age=''
while age != 'quit':
    age = input("Enter your age : ")
    if age == 'quit':
        break
    elif age <= 3:
        print("The ticket is free!")
    elif age > 3 and age <= 12:
        print("The ticket costs $10!")
    else:
        print("The ticket costs $15!")"""

# loop that never ends or infinte loop

x = 1
while x <= 5:
    print(x)
   # x=x+1





