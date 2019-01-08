"""person = {'first name':'Mike','last name':'p','age':'25','city':'tx'}
print("First Name : " + person['first name'] + " , ")
print("Last Name: " + person['last name']+ " , ")
print("Age : " + person['age'] + " , ")
print("City : " + person['city'] )
"""

"""favourite_numbers = {'Chintha':'10','Mary':'15','Deepa':'5','Usha':'9','Sandhya':'5'}
for name,number in favourite_numbers.items():
    #print(name,number)
    print(name + "'s favourite number is : " + number)"""

prog_words = {'List':'Collection of items in particular Order.','Tuple':' Its immutable List.',
              'Dictionary':' Allows to store data in key-value pair','PEP8':'Python Enhancement Proposal 8.',
              'PIP':'Python package installer.','Pygal': 'Package which allows to create visualizations on digital devices',
              'Matplotlib':'Python visualization library','Django':'Python framework for web applications'}
for name,meaning in prog_words.items():
    print(name + ":")
    print("\t"+meaning)
    print("\n")