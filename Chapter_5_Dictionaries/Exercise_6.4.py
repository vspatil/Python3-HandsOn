"""rivers = {'nile':'Egypt','Salinas':'California','Thames':'London'}

for river,cntry in rivers.items():
    print("The " + river + " runs through " + cntry + ".")


print("\n")
for river in rivers.keys():
    print(river)

print("\n")
for cntry in rivers.values():
    print(cntry) """

favoutite_languages = {'Brad':'SQL','Santosh':'Golang','Vani':'Python','Adam':'C','Mike':'C++'}
people = ['Adam','Mike','Charlie','TOM']

for name,lang in favoutite_languages.items():
    print(name + "'s favourite language is : " + lang)

for person in people:
    if person in favoutite_languages:
        print(person + " , Thank you for taking the poll!")
    else:
        print(person + " , Please take a language poll!")