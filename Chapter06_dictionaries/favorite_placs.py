'''
Created on Sep 10, 2019

@author: achaturvedi
'''

favorite_places = {'Satendra' : ['Manali', 'Ladakah', 'Darjelling'],
                   'Ramesh' : ['Kullu', 'Dalhousie', 'Jammu'],
                   'Deepak' : ['Rameshwaram', 'Shimla', 'Gangtok']
                   }

for name, places in favorite_places.items():
    print("\nFavorite palces of "+name+", are: ")
    for place in places:
        print(place)