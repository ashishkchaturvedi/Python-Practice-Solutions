'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import json

number = [1, 2, 3, 4, 5, 6, 7, 8]

filename = 'numbers.json'

with open(filename, 'w') as file_object:
    json.dump(number, file_object)