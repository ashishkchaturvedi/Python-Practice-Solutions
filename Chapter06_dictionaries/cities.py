'''
Created on Sep 10, 2019

@author: achaturvedi
'''
cities = {
    'Delhi' : {
        'Country' : 'India',
        'population' : 2000000,
        'fact' : 'is capital of India'
        },
    'Mumbai' : {
        'Country' : 'India',
        'population' : 3000000,
        'fact' : 'is the financial capital of India'
        },
    'Shimla' : {
        'Country' : 'India',
        'population' : 250000,
        'fact' : 'is the summer capital of India'
        }
    }

for city_name, city_info in cities.items():
    print("\n"+city_name+", is in "+city_info['Country'])
    print("\tThe population of "+city_name+" is "+str(city_info['population']))
    print("\t"+city_name+", "+city_info['fact'])