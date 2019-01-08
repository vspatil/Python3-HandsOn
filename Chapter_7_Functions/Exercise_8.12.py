#8.12
"""
def make_sandwich(*list_of_items):
    print("\nFollowing items needs to be added!")
    for items in list_of_items:
        print(items)


make_sandwich('lettuce')
make_sandwich('tomato','onion')
make_sandwich('tomato','onion','cilantro')
"""

#8.13
"""
def user_profile(first,last,**user_info):
    profile ={}
    profile['First Name']= first
    profile['Last Name']= last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile= user_profile('vani','patil',Proffession='Full time mother',Currently='Studing python')
print(user_profile)

"""

#8.14

def make_car(manufacturer,model,**car_info):
    car = {}
    car['Manufacturer'] = manufacturer
    car['Model'] =model
    for key,value in car_info.items():
        car[key] = value
    return car

car = make_car('Subaru','outback',color='Blue',tow_package=True)
print(car)