'''
Created on Sep 6, 2019

@author: achaturvedi
'''
requested_toppings = ['Mushroom', 'Banan Pepper', 'Tomato', 'Green pepper']

for requested_topping in requested_toppings:
    if requested_topping is 'Green pepper':
        print("Sorry, we are out of Green pepper")
    else: 
        print("Adding "+requested_topping +".")

print("Finished making your pizza!")