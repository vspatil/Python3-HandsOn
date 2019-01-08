"""person_0 = {'first name':'Mike','last':'Jonas','Age':'25','city':'tx'}
person_1 = {'first name':'Priyanka','last':'Chopra','Age':'36','city':'nyc'}
person_2 = {'first name':'brad','last':'parnell','Age':'30','city':'wa'}
people = [person_0,person_1,person_2]
for person in people:
  #print("My name is %s %s; My age is %s; I am from %s" % (person['first name'], person['last'], person['Age'], person['city']))
   print("my name is {},{},{},{}".format(person['first name'],person['last'],person['Age'],person['city']))
  """

"""
# example of dictionary inside a list
dog = {'animal_type' : 'dog','owner':'john'}
cat = {'animal_type':'cat','owner':'mike'}
pets = [dog,cat]

for pet in pets:
    print("{}'s owner is: {}".format(pet['animal_type'],pet['owner']))"""

"""
#example of list inside a dictionary
favourite_places ={'mike':['tahoe','yesomite','la'],'john':['la','vegas','az'],'brad':['wa','nyc','boston']}
for name,places in favourite_places.items():
    print ("\n" + name.title()+"'s favourite places are:")
    for place in places:
        print("\t" + place.title())"""

"""
#example of list inside a dictionary
favourite_numbers = {'chintha': ['10','20','30'],'Usha':['100','200','300'],'Mary':['200','500','700']}
for name,numbers in favourite_numbers.items():
    print("\n" + name.title()+"'s favourite numbers are:")
    for num in numbers:
        print("\t"+ num)
"""

#example of dictionary inside a dictionary
cities = {
    'CA' : {'Country':'US','Coast':'West','Desc':'Full of beaches'},
    'NYC':{'Country':'US','Coast':'EAst','Desc':'Full of ice'},
    'seattle':{'Country':'US','Coast':'west','Desc':'Full of rain'},

}
for city,city_info in cities.items():
    print("\nCity name:" + city.title())
    print("\n Its in:" + city_info['Country']+ " locatesd on :"+ city_info['Coast']+ " ,it is " + city_info['Desc'])


