#9.13
"""
from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['Brad'] = 'SQL'
favourite_languages['Adam'] = 'ERP'
favourite_languages['Mike'] = 'Python'
favourite_languages['Chris'] = 'JAVA'

for name , language in favourite_languages.items():
    print( name.title() + " 's favourite language is : " + language.title())

"""

#9.14
#from random import randint
#x = randint(1,6)

#print(x)
from random import randint
class dice():

    def __init__(self,sides):
        self.sides = sides

    def roll_dice(self):
        x= randint(1,self.sides)
        print( "Random number now we got is : " + str(x))

d= dice(20)
d.roll_dice()
