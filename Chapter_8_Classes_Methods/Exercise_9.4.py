#9.4
"""
class resturant():

    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 20

    def describe_resturant(self):
        print("Name of the resturant is :" + self.name)
        print("Available cuisines in this resturant are :" + self.type)
        print("Number of customers served: "+ self.number_served)

    def open_resturant(self):
        print(self.name + " will be open at 11 Am in the morning!")

    def set_number_served(self):
        print(str(self.name + " Served " + str(self.number_served) + " customers today!"))

    def increment_number_served(self,no):
        self.number_served = no
        print( self.name + " served " + str(self.number_served) + " customers on this day!")



r = resturant('Radhe Chaat','Indian')
r.number_served = 100
r.set_number_served()
r.increment_number_served(200)
"""

#9.5


class user():

    def __init__(self,fname,lname,user_info,login_attempts):
        self.fname= fname
        self.lname=lname
        self.user_info= user_info
        self.login_attempts = login_attempts

    def describe_user(self):
        print("My full name is : " + self.fname + ' ' + self.lname)

    def greet_user(self):
        print("Hello " + self.fname + ' ' + self.lname)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.fname + " has " + str(self.login_attempts )+ " login attempts")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.fname + "you have reached max login attempts" + "\n we are resetting it to 0!")


u = user('Vani','Patil','mother',1)
u.lname
u.fname
u.describe_user()
u.greet_user()
u.increment_login_attempts()
u.reset_login_attempts()
