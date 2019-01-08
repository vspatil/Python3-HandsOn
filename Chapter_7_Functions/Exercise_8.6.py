#8.6
"""
def city_country(city,country):
        formated_str = '"'+ city + ", " + country +'"'
        print(formated_str)
        return formated_str
city_country('Bangalore','India')
 """
#8.7

def make_album(name,title,no_of_tracks=''):
    album = {'Artist_name':name,'Album_Title':title}
    if no_of_tracks:
        album['tracks']=no_of_tracks

    print(album)
    return album

while True:
    print("Please enetr q to quit")
    name = input("Please enter Artist name : ")
    if name == 'q':
        break
    title = input("Please enter title of the album : ")

    if title == 'q':
        break
    make_album(name,title)

#make_album('Vijay','Rajkumar')
#make_album('Rehman','Dilse')
#make_album('Taylor_Swift','Delicate')
#make_album('Vijay','Rajkumar','5')
