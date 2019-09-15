'''
Created on Sep 14, 2019

@author: achaturvedi
'''
from Chapter9_classes import car

new_car = car.Car('audi', 'a4', 2016)

description = new_car.get_descriptive_name()
print(description)
new_car.odometer_reading = 85
new_car.read_odometer()