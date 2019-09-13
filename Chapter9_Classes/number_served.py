'''
Created on Sep 13, 2019

@author: achaturvedi
'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served = 0
        
    def describe_restaurant(self):
        print("\n" + self.restaurant_name + " offers " + self.cuisine_type + " cuisine")
        
    def open_restaurant(self):
        print("The restaurant is now open.")
        
    def served_count(self):
        print("Till now we have served "+ str(self.served) + " customers")
        
    def increment_count(self, count):
        self.served += count
        
restaurant = Restaurant('Bheemas', 'Indian')

restaurant.describe_restaurant()

restaurant.open_restaurant()

restaurant.served_count()

restaurant.increment_count(12)
        
restaurant.served_count()
    