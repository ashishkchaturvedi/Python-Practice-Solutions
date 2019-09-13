'''
Created on Sep 12, 2019

@author: achaturvedi
'''
def describe_pet(animal_type, animal_name):
    print("\nI have a "+animal_type.title())
    print("\tName of my "+ animal_type.title() +" is:" + animal_name.title())
    
describe_pet('dog', 'Ronny')
describe_pet('cat', 'robby')