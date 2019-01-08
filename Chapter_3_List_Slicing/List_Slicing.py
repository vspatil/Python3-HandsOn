""" list slicing """
'''numbers = [2,10,45,23,56]
print("The first three items in the list are :" + str(numbers[:3]))
print("Middle three elements from the list are :" + str(numbers[1:4]))
print("Last three elements from the list are :" + str(numbers[-3:]))'''

""" looping through the for loop """
friend_pizzas = ['pepproni','cheese','veggie']
my_pizzas = friend_pizzas [:]
#print(friend_pizzas)
#print(my_pizzas)
friend_pizzas.append('margretta')
#print (friend_pizzas)
my_pizzas.append('paneer')
#print(my_pizzas)

mp = []
for mypizz in my_pizzas:
    mp.append(mypizz)
print("My favourite pizzas are :" + str(mp))

fp=[]
for frndpizz in friend_pizzas:
    fp.append(frndpizz)
print("My friends favourite pizzas are :" + str(fp))
