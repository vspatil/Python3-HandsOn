#9.6

class resturant():

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_resturant(self):
        print("Name of the resturant is :" + self.name)
        print("Available cuisines in this resturant are :" + self.type)

    def open_resturant(self):
        print(self.name + " will be open at 11 Am in the morning!")

class IceCreamStand(resturant):

    def __init__(self,name,type):
        super().__init__(name,type)
        self.fla = ['Pista','Vanilla']

    def flavours(self):
        print("This resturant has these available ice cream flavours : " + str(self.fla))


#r = IceCreamStand ('Raadhe chaat','Indian')
#r.describe_resturant()
#r.flavours()

#9.7

class user():
    
    def __init__(self,fname,lname,user_info):
        self.fname= fname
        self.lname=lname
        self.user_info= user_info

    def describe_user(self):
        print("My full name is : " + self.fname + ' ' + self.lname)

    def greet_user(self):
        print( "Hello " + self.fname + ' ' + self.lname)

#9.8
class Privileges():

    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban post']

    def show_privileges(self):
        print("Admin has these available rights : " +  str(self.privileges))

class Admin(user):

    def __init__(self,fname,lname,user_info):
        super().__init__(fname,lname,user_info)
        #self.privileges = ['can add post' , 'can delete post','can ban post']
        self.privileges = Privileges()

    def show_privileges(self):
        print("Admin has these available privileges : " + str(self.privileges))


#a = Admin('Vani','Patil','Mother')
#a.describe_user()
#a.privileges
#a.privileges.show_privileges()



