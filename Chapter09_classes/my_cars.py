'''
Created on Sep 14, 2019

@author: achaturvedi
'''
from Chapter9_classes import car
from Chapter9_classes import electric_car

my_beetle = car.Car('Volkswagen', 'Beetle', 2016)
my_tesla = electric_car.ElectricCar('Tesla', 'Model s', 2019)

print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())