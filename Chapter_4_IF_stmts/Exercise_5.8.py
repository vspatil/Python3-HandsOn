"""users = []

#['admin','Mike','Eric','Brad','Adam']

if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + " , Would you like to see a status report?")
        else:
            print("Hello " + user + " , thank you for logging again!")
else:
    print("we need to find some users") """


"""current_users = ['Adam','nick','Jhon','Brad','Mike']
new_users = ['Alex','Nick','Charlie','Rigo','mike']

modified_users = []
for user in current_users:
    user = user.upper()
    modified_users.append(user)
#print(modified_users)
for new_user in new_users:
    new_user1 = new_user.upper()
    if new_user1 in modified_users:
        print("Please enter new username," + new_user + " is already used...")
    else:
        print(new_user + " is available...")"""

num_list = [1,2,3,4,5,6,7,8,9]

for num in num_list:
    if num == 1:
        print(str(num) + "st")
    elif num == 2 or num == 3:
        print(str(num) + "nd")
    else:
        print(str(num) + "th")
