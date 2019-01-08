"""8.3 def make_shirt(size,text):
    #print("I have a Shirt of size " + size + " ,with a text " + text + " on it!")

#calling function with postional parameters
#make_shirt('small','I love India')

#calling function with keyword parameters
#make_shirt(size='small',text='I love India') """

"""
#8.4
def make_shirt(size='large',text='i love python'):
    print("I have a Shirt of size " + size + " ,with a text " + text + " on it!")


make_shirt()
make_shirt(size='large')
make_shirt(size='small')
make_shirt(text='I love to code') """

#8.5
def describe_city(city,country='India'):
    print(city + " is in " + country)

describe_city('Bangalore','India')
describe_city('Bangalore')
describe_city('Mysore')
describe_city('NYC')

