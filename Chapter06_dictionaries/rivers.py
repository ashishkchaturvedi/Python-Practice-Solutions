'''
Created on Sep 9, 2019

@author: achaturvedi
'''
rivers = {
    'Gange' : 'India',
    'Nile' : 'Egypt',
    'Thames' : 'England',
    'Missisippi' : 'USA',
    }

for river, country in rivers.items():
    print("\nThe "+river+" runs through "+country)
    
print("\n")
for river in rivers.keys():
    print(river)
    
print("\n")
for country in rivers.values():
    print(country)