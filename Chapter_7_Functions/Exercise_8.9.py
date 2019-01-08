#8.9
"""def show_magicians(names):
    for name in names:
        print("Hello " + name.title())

names = ['TOM','CHRIS','Michel']
show_magicians(names)
"""
#8.10
"""
names = ['TOM','CHRIS','Michel']
modified_names=[]
def make_great(names):
    for name in names:
        name = name + " the great" .title()
        modified_names.append(name)
        print(modified_names)

def show_magicians(modified_names):
    for name in modified_names:
        print("Hello " + name.title())

make_great(names)
show_magicians(modified_names)
show_magicians(names)
"""


#8.11
names = ['TOM','CHRIS','Michel']
name_new = names[:]
modified_names = []
list_names = modified_names
print(list_names)

def make_great(name_new):
    while name_new:
        name = name_new.pop()
        name = name + " the great" .title()
        print(name)
        modified_names.append(name)
    return modified_names

def show_magicians(modified_names):
    for name in modified_names:
        print("Hello " + name.title())


make_great(name_new)
show_magicians(modified_names)
show_magicians(names)
