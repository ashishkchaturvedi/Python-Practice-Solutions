'''
Created on Sep 15, 2019

@author: achaturvedi
'''
def get_formatted_name(city, country, population = ''):
    
    if population:
        
        location = city + ', ' + country + ' - ' + population
        
    else:
        
        location = city + ', ' + country
    
    return location.title()

