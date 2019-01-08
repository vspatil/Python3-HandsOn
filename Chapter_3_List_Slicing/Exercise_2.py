''' Counting to twenty'''
"""
numbers = []
for number in range(1,21):
    numbers.append(number)
print(numbers) """

"""Counting upto 1 milliom"""
'''
numbers = []
for number in range(1,1000001):
    numbers.append(number)
print(numbers[-1])
print(min(numbers))
print(max(numbers))
print(sum(numbers))'''

""" Printing odd numbers"""

numbers = []
for number in range(1, 21,2):
    #print(number)
    numbers.append(number)
print(numbers)

""" print multiples of three"""

numbers = []
for number in range(3,31,3):
    #print(number)
    numbers.append(number)
print(numbers)

""" displying Cube root of a number"""

numbers = []

for number in range(1,11):
    number = number ** 3
    #print(number)
    numbers.append(number)
print(numbers)

""" List comprehension for first 10 cubes"""
cube = [number**3 for number in range(1,11)]
print(cube)