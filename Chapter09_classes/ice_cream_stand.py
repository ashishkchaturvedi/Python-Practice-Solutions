'''
Created on Sep 14, 2019

@author: achaturvedi
'''
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("\n" + self.restaurant_name + " offers " + self.cuisine_type + " cuisine")
        
    def open_restaurant(self):
        print("The restaurant is now open.")
        
class IceCreamStand(Restaurant):
    
    def __init__(self, flavors):
        self.flavors = flavors
        
    def describe_flavors(self):
        print("The list of flavors are: ")
        for flavor in self.flavors:
            print(flavor)
            
flavors = ['Vanilla', 'Strawberry', 'Banana', 'Mango']

my_restaurant = IceCreamStand(flavors)

my_restaurant.describe_flavors()