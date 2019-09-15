'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import json

filename = 'numbers.json'

with open(filename) as file_obj:
    numbers = json.load(file_obj)
    
print(numbers)