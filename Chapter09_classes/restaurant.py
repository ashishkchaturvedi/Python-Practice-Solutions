'''
Created on Sep 13, 2019

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
        
        
# restaurant1 = Restaurant('Bheemas', 'Indian')
# restaurant2 = Restaurant('Chipotle', 'Mexican')
# restaurant3 = Restaurant('Dominos', 'American')
# 
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()
# 
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()
# 
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant()