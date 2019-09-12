'''
Created on Sep 12, 2019

@author: achaturvedi
'''

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name: ")
    
    place = input("\nWhich is the place in the world you would like to visit: ")
    
    responses[name] = place
    
    repeat = input("\nDo you want others to poll(yes/no): ")
    
    if repeat.title() == 'No':
        polling_active = False
        
for name, place in responses.items():
    print("\n" + name.title() + ", wants to visit: " + place.title())