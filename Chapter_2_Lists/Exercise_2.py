''' Inviting friends for dinner'''
guests = ['usha','tripta','Mary','Sandhya']
for guest in guests:
    print("Hi " + guest.title() + " , Please come home for dinner today!")
    print("Please treat this as personal invitation.\n")
print("Sandhya can't make it to the dinner!\n")

""" since one friend cant make it,so inviting other friend """
guests[3]= 'kavita'
print("New guest list for dinner : " + str(guests) + "\n" )

for guest in guests:
    print("Hi " + guest.title() + " , Please come home for dinner today!")
    print("Please treat this as personal invitation.")
    print("My address is 20350 Stevens Creek Blvd,Cupertino.\n")

print(" Hello Girls found bigger table for dinner,can invite three more people!\n")

guests.insert(0, 'Hardev')
print(guests)
guests.insert(2,'Phani')
print(guests)
guests.append('loyola')
print(guests)

for guest in guests:
    print("Hi " + guest.title() + " , Please come home for dinner today!")
    print("Please treat this as personal invitation.")
    print("My address is 20350 Stevens Creek Blvd,Cupertino.\n")

name1 = guests.pop()
print("I am very sorry " + name1 + ", I cant invite you for dinner.")
print(len(guests))
name2 = guests.pop()
print("I am very sorry " + name2 + ", I cant invite you for dinner.")
name3 = guests.pop()
print("I am very sorry " + name3 + ", I cant invite you for dinner.")
name4 = guests.pop()
print("I am very sorry " + name4 + ", I cant invite you for dinner.")
name5 = guests.pop()
print("I am very sorry " + name5 + ", I cant invite you for dinner.")
print(guests)
name6 = guests.pop()
print("I am very sorry " + name6 + ", I cant invite you for dinner.")
guests.insert(1,'Tripta')
print(guests)

for guest in guests:
    print("Hello Dear you both are still invited for dinner")
del guests[0]
del guests[1]

print (guests)