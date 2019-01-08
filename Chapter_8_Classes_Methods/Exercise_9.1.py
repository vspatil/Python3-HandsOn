"""
class resturant():

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_resturant(self):
        print("Name of the resturant is :" + self.name)
        print("Available cuisines in this resturant are :" + self.type)

    def open_resturant(self):
        print(self.name + " will be open at 11 Am in the morning!")


r = resturant('Radhe chat','Indian')
print(r.name)
print(r.type)
r.describe_resturant()
r.open_resturant()

p = resturant ('Thai','Thailand')
q= resturant('ICC','Indian')
print (p.name)
print(p.type)
p.describe_resturant()
q.describe_resturant()
q.open_resturant()
p.open_resturant()

"""

#9.3

class user():

    def __init__(self,fname,lname,user_info):
        self.fname= fname
        self.lname=lname
        self.user_info= user_info

    def describe_user(self):
        print("My full name is : " + self.fname + ' ' + self.lname)

    def greet_user(self):
        print( "Hello " + self.fname + ' ' + self.lname)


u = user('Vani','Patil','mother')
u.lname
u.fname
u.describe_user()
u.greet_user()
