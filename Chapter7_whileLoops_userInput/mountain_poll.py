'''
Created on Sep 12, 2019

@author: achaturvedi
'''
responses = {}

polling_active = True

while polling_active:
    
    name = input("\nWhat is your name: ")
    
    response = input("\nWhich mountain you want to climb someday: ")
    
    responses[name] = response
    
    repeat = input("\nWould you like to let another person respond(yes/no): ")
    
    if(repeat.title() == 'No'):
        polling_active = False
        
        
for name, response in responses.items():
    print(name.title() + ", wants to climb " + response.title() + " mountain")
    