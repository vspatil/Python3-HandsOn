"""sandwich_orders = ['chicken_sandwich','veg_sandwich','chicken_sandwich','cheese_sandwich','chicken_sandwich']
finished_sandwiches =[]

while sandwich_orders:
    current = sandwich_orders.pop()
    print(" I will make your " + current )

    finished_sandwiches.append(current)

print("\nFollowing pizzas have made today!")
for sandwich in finished_sandwiches:
    print(sandwich)
"""

"""
sandwich_orders = ['chicken_sandwich','veg_sandwich','chicken_sandwich','cheese_sandwich','chicken_sandwich']
finished_sandwiches =[]

print(" there are no chicken sandwiches!")
while 'chicken_sandwich' in sandwich_orders:
    sandwich_orders.remove('chicken_sandwich')

print(sandwich_orders)
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

print("\nFollowing pizzas have made today!")
for sandwich in finished_sandwiches:
    print(sandwich) """

responses = {}

polling_status = True

while polling_status:
    name = input("Please enter your name?")
    prompt = input("If you could visit one place in the world,where would you go? ")
    #print(prompt)
    responses[name]= prompt

    repeat =  input("Would you like to let another person respond?")
    if repeat == 'no':
        polling_status= False

print("\n.....Poll Results....")
for name,response in responses.items():
    print(name + " would like to visit " +response)
