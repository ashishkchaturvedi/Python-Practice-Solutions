'''
Created on Sep 6, 2019

@author: achaturvedi
'''
requested_toppings = ['Mushroom']

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping +".")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza")