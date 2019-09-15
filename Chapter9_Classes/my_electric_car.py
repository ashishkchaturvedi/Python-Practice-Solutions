'''
Created on Sep 14, 2019

@author: achaturvedi
'''
from Chapter9_classes import car

my_tesla = car.ElectricCar('tesla', 'model s', 2019)

description = my_tesla.get_descriptive_name()
print(description)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()