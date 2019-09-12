'''
Created on Sep 11, 2019

@author: achaturvedi
'''
prompt = "\nEnter the name of cities you have visited: "

prompt += "\nEnter 'quit' when you are done."

while True:
    city = input(prompt)
    
    if city == 'quit':
        break;
    else:
        print("\nI would love to visit: "+ city)