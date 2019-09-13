'''
Created on Sep 11, 2019

@author: achaturvedi
'''
prompt = "\nEnter the topping for pizza: "
prompt += "\nEnter 'quit' to exit"

topping = ''

while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print("\nAdding "+ topping +" to your pizza")
    
    
